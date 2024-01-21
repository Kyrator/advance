import logging
import sys
from typing import Union, Callable
from operator import sub, mul, truediv, add


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - name=%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

Numeric = Union[int, float]


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    logger.info('Start def string_to_operator')
    if not isinstance(value, str):
        logger.exception("{e} \'{value}\'".format(e="wrong operator type", value=value))
        raise "wrong operator type"
        # logger.exception("{e} \'{value}\'".format(e="wrong operator type", value=value))
        # raise ValueError
        # print("wrong operator type", value)
        # raise ValueError("wrong operator type")

    if value not in OPERATORS:
        logger.exception("{e} \'{value}\'".format(e="wrong operator value", value=value))
        raise "wrong operator value"
        # logger.exception("{e} \'{value}\'".format(e="wrong operator value", value=value))
        # raise ValueError
        # print("wrong operator value", value)
        # raise ValueError("wrong operator value")
    return OPERATORS[value]
