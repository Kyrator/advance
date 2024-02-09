import logging
import logging.config
import logging.handlers
import sys
import json

# class myHTTPHandler(logging.handlers.HTTPHandler):
#   def mapLogRecord(self,record):
#     trec={'record':json.dumps(record.__dict__)}
#     return trec

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(message)s"
        }
    },
    "handlers": {
        "server_handler_post": {
            "class": "logging.handlers.HTTPHandler",
            "host": '127.0.0.1:3000',
            "url": '/log',
            "method": "POST",
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
        },
        "server_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs",
            "mode": 'a',
            "maxBytes": 10000000,
            "backupCount": 10,
        }
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["console", "server_handler_post"],
            # "propagate": False,
        },
        "utils": {
            "level": "DEBUG",
            "handlers": ["console"],
            # "propagate": False,
        },
        "server": {
            "level": "DEBUG",
            "handlers": ["console"],
            # "propagate": False,
            }
    },

    # "filters": {},
    # "root": {} # == "": {}
}



