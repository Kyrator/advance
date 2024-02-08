import logging
import logging.config
import string
import sys


class MyFilter(logging.Filter):
    def __init__(self):
        super().__init__()

    def filter(self, record):
        if record.msg.isascii():
            return True
        return False


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(message)s"
        }
    },
    'filters': {
        'my_filter': {
            '()': MyFilter,
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            'filters': ['my_filter'],

        }
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["console"],
            # "propagate": False,
        }
    },

    # "root": {} # == "": {}
}
