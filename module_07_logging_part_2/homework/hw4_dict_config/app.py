import logging
import logging.config
import sys
from utils import string_to_operator
from dict import get_logger

logger = get_logger("app")


def calc(args):
    logger.debug("Arguments: {args}".format(args=args))
    # print("Arguments: ", args)

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as err:
        logger.error("ValueError", exc_info=False)

    try:
        num_2 = float(num_2)
    except ValueError as err:
        logger.error("ValueError", exc_info=False)

    operator_func = string_to_operator(operator)
    result = operator_func(num_1, num_2)

    # print("Result: ", result)
    logger.debug("Result: {}".format(result))

    # print(f"{num_1} {operator} {num_2} = {result}")
    logger.debug(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    # calc(sys.argv[1:])
    calc('2+3')
    calc('3.2')


