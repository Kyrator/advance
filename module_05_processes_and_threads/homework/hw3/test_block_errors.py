import unittest
from block_errors import BlockErrors


class TestBlockError(unittest.TestCase):
    def test_err_types(self):
        dict_err_types = {ZeroDivisionError, TypeError}
        try:
            with BlockErrors(dict_err_types):
                a = 1 / 0
        except:
            self.assertRaises('Выполнено без ошибок')
        # print(self)
        # .assertTrue('Выполнено без ошибок' in self.)
        """ Выполнено без ошибок """

    def test_err_types2(self):
        dict_err_types2 = {ZeroDivisionError}
        try:
            with BlockErrors(dict_err_types2):
                a3 = 1 / '0'
            print('Выполнено без ошибок')
        except TypeError:
            self.assertRaises(TypeError)

        """TypeError: unsupported operand type(s) for /: 'int' and 'str'"""

    def test_outer_err_types3(self):
        dict_outer_err_types = {TypeError}
        try:
            with BlockErrors(dict_outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a1 = 1 / '0'
                print('Внутренний блок: выполнено без ошибок')
            print('Внешний блок: выполнено без ошибок')
        except:
            self.assertRaises('Внешний блок: выполнено без ошибок')

        """Внешний блок: выполнено без ошибок"""

    def test_err_types4(self):
        dict_err_types = {Exception}
        try:
            with BlockErrors(dict_err_types):
                a2 = 1 / '0'
            print('Выполнено без ошибок')
        except:
            self.assertRaises('Выполнено без ошибок')

        """Выполнено без ошибок"""


if __name__ == '__main__':
    unittest.main()
