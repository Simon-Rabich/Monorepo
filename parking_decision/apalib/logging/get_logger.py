#!/usr/bin/env python3
#    ___                      _
#   / __\   _ _ __ ___  _ __ | |_ ___  _ __ ___
#  / / | | | | '_ ` _ \| '_ \| __/ _ \| '_ ` _ \
# / /__| |_| | | | | | | |_) | || (_) | | | | | |
# \____/\__, |_| |_| |_| .__/ \__\___/|_| |_| |_|
#       |___/          |_|
#
# CYMPTOM LABS Copyright 2022. All rights reserved.
#
# Author: Naum Raviz (nraviz@tenable.com) on 02/08/2022

# STD packages
import inspect
import os
import logging
import logging.config
import socket
import sys
from functools import lru_cache
from os.path import expanduser
from typing import Any, MutableMapping, Tuple, Optional
import urllib3

from apalib.configurations.get_config import get_config


def parse_env_string(value: str):
    return value and expanduser(value)

LOGS_PATH = get_config()["LOGS_DIR"]

ACTIVITY_LEVEL_NUM = 1337
logging.ACTIVITY_LEVEL_NUM = ACTIVITY_LEVEL_NUM
logging.__all__ += ["ACTIVITY"]
logging.addLevelName(ACTIVITY_LEVEL_NUM, "ACTIVITY")


def activity(self, message, *args, **kwargs):
    if not (
            message.startswith("FOUND:")
            or message.startswith("NEW:")
            or message.startswith("RUN:")
    ):
        raise ValueError(
            f"Bad message format specified. Make sure message starts with 'FOUND:' 'NEW:' or 'RUN:'.\n message: {message}"
        )
    if self.isEnabledFor(ACTIVITY_LEVEL_NUM):
        self._log(ACTIVITY_LEVEL_NUM, message, args, **kwargs)


logging.Logger.activity = activity

# LOGS_PATH = CymptomConfig.get_config().misc.log_path
os.makedirs(LOGS_PATH, exist_ok=True)


@lru_cache(maxsize=1)
def get_fqdn():
    try:
        if not os.environ.get("CYMPTOM_TEST"):
            return socket.getfqdn()
        else:
            return ""
    except KeyboardInterrupt:
        raise
    except Exception as e:
        return ""


class ContextFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def filter(self, record):
        record.fqdn = getattr(record, "fqdn", "")  # get_fqdn() makes it too slow.
        record.entity = getattr(record, "entity", "")
        return True


LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"context_filter": {"()": ContextFilter}},
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(name)-30s %(entity)s [%(levelname)s]: %(message)s",
            # "datefmt": "%H:%M:%S",
            "datefmt": "%d/%m/%y-%H:%M:%S",
            "stream": sys.stdout,
        },
        "detailed": {
            "format": "%(fqdn)s> (%(asctime)s) %(name)-30s %(entity)s [%(levelname)s]: %(message)s"
        },
        "cymptom_activity": {"format": "%(asctime)s %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filters": ["context_filter"],
            # "filename": sys.stdout
        },
        "file_info": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "filename": os.path.join(LOGS_PATH, "info.log"),
            "formatter": "detailed",
            "maxBytes": 10485760,
            "backupCount": 3,
            "encoding": "utf8",
            "filters": ["context_filter"],
        },
        "file_error": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "filename": os.path.join(LOGS_PATH, "error.log"),
            "formatter": "detailed",
            "maxBytes": 10485760,
            "backupCount": 3,
            "encoding": "utf8",
            "filters": ["context_filter"],
        },
        "file_debug": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "filename": os.path.join(LOGS_PATH, "debug.log"),
            "formatter": "detailed",
            "maxBytes": 10485760,
            "backupCount": 3,
            "encoding": "utf8",
            "filters": ["context_filter"],
        },
        "file_warning": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "WARNING",
            "filename": os.path.join(LOGS_PATH, "warning.log"),
            "formatter": "detailed",
            "maxBytes": 10485760,
            "backupCount": 3,
            "encoding": "utf8",
            "filters": ["context_filter"],
        },
        "file_activity": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ACTIVITY",
            # <-- Set the activity.log into the shared volume for web to fetch it into activity log
            "filename": os.path.join(LOGS_PATH, "activity.log"),
            "formatter": "cymptom_activity",
            "maxBytes": 2097152,
            "backupCount": 0,
            "encoding": "utf8",
        },
    },
    "loggers": {
        "": {
            "handlers": [
                "file_info",
                "console",
                "file_error",
                "file_debug",
                "file_warning",
                "file_activity",
            ],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

# TODO: add `exc_info=log.getEffectiveLevel() == logging.DEBUG` to error configuration?

logging.config.dictConfig(LOG_CONFIG)

# shhhh you're making too much noise
urllib3.disable_warnings()
logging.getLogger("neo4j").setLevel(logging.WARN)
logging.getLogger("paramiko").setLevel(logging.WARN)
logging.getLogger("paramiko.transport").setLevel(logging.WARN)
logging.getLogger("kafka").setLevel(logging.ERROR)
logging.getLogger("snowflake.connector").setLevel(logging.ERROR)
logging.getLogger("botocore").setLevel(logging.ERROR)
logging.getLogger("pika").setLevel(logging.ERROR)
logging.getLogger("chardet").setLevel(logging.ERROR)
logging.getLogger("asyncio").setLevel(logging.WARN)
logging.getLogger("urllib3.connectionpool").setLevel(logging.INFO)
logging.getLogger("urllib").setLevel(logging.INFO)
logging.getLogger("sqlitedict").setLevel(logging.INFO)
logging.getLogger("adal-python").setLevel(logging.WARN)
logging.getLogger("msrest").setLevel(logging.WARN)
logging.getLogger("msal").setLevel(logging.WARN)
logging.getLogger("azure.core.pipeline.policies").setLevel(logging.WARN)
logging.getLogger("faker.factory").setLevel(logging.WARN)
# TODO: lower to warn once i find a workaround for pulling from redis queue without
#   "rsmq.cmd.ReceiveMessageCommand  [WARNING]: NoMessageInQueue: Exception while processing ReceiveMessageCommand:
#   Queue 'collector_67_attacks' has no messages waiting"
logging.getLogger("rsmq").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("BeautifulSoup").setLevel(logging.ERROR)
logging.getLogger("azure.identity._internal.interactive").setLevel(logging.ERROR)

logging.getLogger("boto3.resources.action").setLevel(logging.WARN)
logging.getLogger("boto3.resources.factory").setLevel(logging.WARN)
logging.getLogger("boto3.resources.model").setLevel(logging.WARN)
logging.getLogger("boto3.resources.collection").setLevel(logging.WARN)

logging.getLogger("SplunkHandler").setLevel(logging.WARN)

logging.getLogger("ddtrace.sampler").setLevel(logging.INFO)
logging.getLogger("ddtrace.tracer").setLevel(logging.INFO)
logging.getLogger("ddtrace.internal.writer").setLevel(logging.INFO)


class CymptomLoggerAdapter(logging.LoggerAdapter):
    extra: dict

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra["entity"] = ""

    def process(
            self, msg: Any, kwargs: MutableMapping[str, Any]
    ) -> Tuple[Any, MutableMapping[str, Any]]:
        kwargs["extra"] = self.extra
        return msg, kwargs

    def activity(self, msg, *args, **kwargs):
        msg, kwargs = self.process(msg, kwargs)
        self.logger.activity(msg, *args, **kwargs)

    def set_current_entity(self, entity: "Entity" = None, key: str = None, ent_type: str = None):
        """
        Adds the entity to all foreword messages in the form of "entity_cls_name<entity_key>"
        :param ent_type: type of the entity
        :param key: key
        :param entity: a dataclass Entity
        """
        # TODO: add this to all services execute task
        from cymptomlib.objects.entities import Entity

        if entity:
            if hasattr(type(entity), "key"):
                self.extra["entity"] = f"({type(entity).__name__}<{entity.key}>)"

        else:
            if key and ent_type:
                self.extra["entity"] = f"({ent_type}<{key}>)"

    def clear_current_entity(self):
        """
        clears the current set entity from all foreword log messages"
        """
        self.extra["entity"] = ""


def get_logger(name: Optional[str] = None) -> CymptomLoggerAdapter:
    if name is None:
        caller = inspect.currentframe().f_back
        name = caller.f_globals['__name__']
    return CymptomLoggerAdapter(
        logger=logging.getLogger(name), extra={}  # "fqdn": get_fqdn()}
    )
