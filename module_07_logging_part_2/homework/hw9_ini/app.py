import logging.config
from dict_config import dict_config

logging.config.dictConfig(dict_config)
appLogger = logging.getLogger('appLogger')


appLogger.debug("DEBUG")
appLogger.info("INFO")
appLogger.warning("WARNING")

