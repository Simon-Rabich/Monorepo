import asyncio
import json

import aio_pika
from bson import json_util


async def main() -> None:
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@localhost/",
    )

    async with connection:
        routing_key = "blog.posts.create"

        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=json.dumps({"ping": "pong"}, default=json_util.default).encode()),
            routing_key=routing_key,
        )


if __name__ == "__main__":
    asyncio.run(main())
