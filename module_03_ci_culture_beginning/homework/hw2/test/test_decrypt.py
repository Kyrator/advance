import unittest


from module_03_ci_culture_beginning.homework.hw2.decrypt import decrypt


class TestDecrypt(unittest.TestCase):
    def test_decrypt_point_in_middle(self):
        """Группировка когда точка находится посередине"""
        items = (
            {'input': 'абраа..-кадабра', 'output': 'абра-кадабра'},
            {'input': 'абраа..-.кадабра', 'output': 'абра-кадабра'},
            {'input': 'абра--..кадабра', 'output': 'абра-кадабра'},
            {'input': 'абрау...-кадабра', 'output': 'абра-кадабра'},
        )

        for item in items:
            with self.subTest(item['input']):
                output = decrypt(
                    item['input'],
                )
                self.assertEqual(
                    output,
                    item['output']
                )

    def test_decrypt_point_in_end(self):
        """Группировка когда точка находится в конце"""
        items = (
            {'input': 'абра-кадабра.', 'output': 'абра-кадабра'},
            {'input': 'абра........', 'output': ''},
            {'input': 'абр......a.', 'output': 'a'},
            {'input': '.', 'output': ''},
        )

        for item in items:
            with self.subTest(item['input']):
                output = decrypt(
                    item['input'],
                )
                self.assertEqual(
                    output,
                    item['output']
                )

    def test_decrypt_digital(self):
        """Группировка когда используются числа"""
        items = (
            {'input': '1..2.3', 'output': '23'},
            {'input': '1.......................', 'output': ''},
        )

        for item in items:
            with self.subTest(item['input']):
                output = decrypt(
                    item['input'],
                )
                self.assertEqual(
                    output,
                    item['output']
                )