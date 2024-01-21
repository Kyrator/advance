import sys
import logging
from utils import string_to_operator


logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('уровень-%(levelname)s логгер-%(name)s время-%(asctime)s номер_строки=%(lineno)d '
                              'сообщение-%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def calc(args):
    logger.info("Arguments: {args}".format(args=args))
    # print("Arguments: ", args)

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        # print("Error while converting number 1")
        # print(e)
        logger.exception("Error while converting number 1 {}".format(e))
        raise ValueError(e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        # print("Error while converting number 1")
        # print(e)
        logger.exception("Error while converting number 2".format(e))
        raise e

    operator_func = string_to_operator(operator)
    result = operator_func(num_1, num_2)

    # print("Result: ", result)
    logger.info("Result: {}".format(result))

    # print(f"{num_1} {operator} {num_2} = {result}")
    logger.info(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    # calc(sys.argv[1:])
    calc('2+3')


