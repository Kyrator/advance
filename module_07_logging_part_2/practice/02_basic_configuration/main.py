import logging


logging.basicConfig()
logger = logging.getLogger()


sub_1 = logging.getLogger('sub_1')
sub_1.setLevel('DEBUG')

sub_sub_1 = logging.getLogger('sub_1.sub_sub_1')
sub_sub_1.propagate = True

sub_2 = logging.getLogger('sub_2')
sub_2.setLevel('INFO')
sub_2.propagate = True

custom_handler = logging.StreamHandler()
logger.addHandler(custom_handler)

formatter = logging.Formatter(fmt="%(name)s || %(levelname)s || %(message)s || %(module)s.%(funcName)s:%(lineno)d")
custom_handler.setFormatter(formatter)




if __name__ == "__main__":
    logger.debug("DEBUG")
    # logger.info("info")
    # logger.warning("WARNING")
    # logger.error("ERROR")
    # logger.critical("CRITICAL")
    # print()
    sub_1.debug("DEBUG")
    # sub_1.info("info")
    # sub_1.warning("WARNING")
    # sub_1.error("ERROR")
    # sub_1.critical("CRITICAL")
    # print()
    sub_2.debug("DEBUG")
    sub_2.info("info")
    # sub_2.warning("WARNING")
    # sub_2.error("ERROR")
    # sub_2.critical("CRITICAL")
    # print()
    sub_sub_1.debug("DEBUG")
    # sub_sub_1.info("info")
    # sub_sub_1.warning("WARNING")
    # sub_sub_1.error("ERROR")
    # sub_sub_1.critical("CRITICAL")
    # print()