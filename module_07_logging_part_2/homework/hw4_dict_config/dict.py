import logging
import logging.config
import sys


class LevelFileHandler(logging.Handler):
    def __init__(self, file_name, mode='a'):
        super().__init__()
        self.file_name = file_name
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        print(message)
        if self.filter(record):
            with open(self.file_name, mode=self.mode) as f:
                f.write(message + '\n')


class LevelFilter(logging.Filter):
    def __init__(self, param):
        super().__init__()
        self.param = param

    def filter(self, record):
        return record.levelname == self.param


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(message)s"
        }
    },
    "filters": {
        'debug_filter': {
            '()': LevelFilter,
            "param": "DEBUG"
        },
        'error_filter': {
            '()': LevelFilter,
            "param": "ERROR"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            # "stream": sys.stdout
        },
        "debug_file": {
            "()": LevelFileHandler,
            "level": "DEBUG",
            "formatter": "base",
            "file_name": "calc_debug.log",
            "mode": "a",
            "filters": ['debug_filter']
        },
        "error_file": {
            "()": LevelFileHandler,
            "level": "ERROR",
            "formatter": "base",
            "file_name": "calc_error.log",
            "mode": "a",
            "filters": ['error_filter']
        },
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["debug_file", "error_file", "console"],
            # "propagate": False,
        }
    },

    # "filters": {},
    # "root": {} # == "": {}
}


def get_logger(name):
    logging.config.dictConfig(dict_config)
    logger = logging.getLogger(name)
    return logger

