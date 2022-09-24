import os
import asyncio
import logging

import aio_pika
from aio_pika.channel import Channel
from aio_pika.queue import Queue
from motor.motor_asyncio import AsyncIOMotorClient
from async_message_handling.src.consumer import Consumer

DEFAULT_QUEUE_PARAMETERS = {
    "durable": True,
    "arguments": {
        "x-queue-type": "quorum",
    },
}


loop = asyncio.get_event_loop()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def _prepare_consumed_queue(channel: Channel) -> Queue:
    if os.environ.get('RABBITMQ_DEAD_LETTER_EXCHANGE_NAME'):
        # auto reroute nacked messages to DLX
        DEFAULT_QUEUE_PARAMETERS["arguments"]["x-dead-letter-exchange"] = os.environ.get('RABBITMQ_DEAD_LETTER_EXCHANGE_NAME')
    queue = await channel.declare_queue(
        os.environ.get('RABBITMQ_QUEUE_NAME'),
        **DEFAULT_QUEUE_PARAMETERS,
    )

    await queue.bind(os.environ.get('RABBITMQ_EXCHANGE_NAME'), "blog.posts.create")

    return queue


async def _prepare_dead_letter_queue(channel: Channel) -> Queue:
    dead_letter_queue: Queue = await channel.declare_queue(
        os.environ.get("RABBITMQ_DEAD_LETTER_QUEUE_NAME"),
        **DEFAULT_QUEUE_PARAMETERS,
    )
    bindings = os.environ.get('RABBITMQ_QUEUE_BINDINGS')
    for routing_key in bindings:
        await dead_letter_queue.bind(os.environ.get('RABBITMQ_DEAD_LETTER_EXCHANGE_NAME'), routing_key)

    return dead_letter_queue


async def main(consumer_class) -> None:
    mongo_db_client = AsyncIOMotorClient({
        'host': "localhost",
        'port': 27017
    })
    rabbitmq_connection = await aio_pika.connect_robust(
        loop=loop,
        url="amqp://guest:guest@localhost/"
    )

    try:
        async with rabbitmq_connection.channel() as channel:
            await channel.set_qos(prefetch_count=100)

            if os.environ.get('RABBITMQ_DEAD_LETTER_ENABLED'):
                await _prepare_dead_letter_queue(channel)

            queue = await _prepare_consumed_queue(channel)

            consumer = consumer_class(
                queue=queue,
                db_client=mongo_db_client,
            )

            await consumer.consume()
    finally:
        await rabbitmq_connection.close()


if __name__ == '__main__':
    try:
        asyncio.run(
            main(Consumer)
        )
    except asyncio.CancelledError:
        logger.info('Main task cancelled')
    except Exception:
        logger.exception('Something unexpected happened')
    finally:
        logger.info("Shutdown complete")