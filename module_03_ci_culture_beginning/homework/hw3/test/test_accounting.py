import unittest

from module_02_linux.homework.hw7.accounting import app, storage


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Конфигурационная функция"""
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()

    def test_add(self):
        """Тестирование функции добавления"""
        items = (
            {'data': '20231113', 'value': '20', 'answer': "Запись произведена {2023: {11: 20, 'total': 20}}"},
            {'data': '20231114', 'value': '20', 'answer': "Запись произведена {2023: {11: 40, 'total': 40}}"},
            {'data': '20231116', 'value': '20', 'answer': "Запись произведена {2023: {11: 60, 'total': 60}}"},
        )

        for item in items:
            with self.subTest(item['data']):
                self.base_url = '/add/' + item['data'] + '/'
                output = self.app.get(self.base_url + item['value']).data.decode()
                self.assertEqual(
                    output,
                    item['answer']
                )

    def test_calculate_year(self):

        """Тестирование функции расчета года"""
        items = (
            {'data': '2023', 'answer': "60"},
            {'data': '2022', 'answer': "2022 год пустой, заполните значения"},
            {'data': '2021', 'answer': "2021 год пустой, заполните значения"},
        )

        for item in items:
            with self.subTest(item['data']):
                self.base_url = '/calculate/' + item['data']
                output = self.app.get(self.base_url).data.decode()
                self.assertEqual(
                    output,
                    item['answer']
                )

    def test_calculate_month(self):
        """Тестирование функции расчет месяца"""
        items = (
            {'data': '2023', 'month': '11', 'answer': "60"},
            {'data': '2021', 'month': '10', 'answer': "10 месяц 2021 года пустой, заполните значения"},
            {'data': '2022', 'month': '05', 'answer': "5 месяц 2022 года пустой, заполните значения"},

        )

        for item in items:
            with self.subTest(item['data']):
                self.base_url = '/calculate/' + item['data'] + '/' + item['month']
                output = self.app.get(self.base_url).data.decode()
                self.assertEqual(
                    output,
                    item['answer']
                )

    def test_add_incorrect_data(self):
        """Тестирование функции расчета некорректная дата года"""
        items = (
            {'data': '2023november13', 'value': 'twenty', 'answer': "Запись произведена {2023: {11: 20, 'total': 20}}"},
        )

        for item in items:
            with self.subTest(item['data']):
                with self.assertRaises(TypeError):
                    self.base_url = '/add/' + item['data'] + '/'
                    output = self.app.get(self.base_url + item['value']).data.decode()
                    self.assertRaises(
                        output,
                        TypeError
                    )

    def test_calculate_year_without_storage(self):
        storage.clear()
        """Тестирование функции расчета года без данных"""

        items = (
            {'data': '2023', 'answer': "2023 год пустой, заполните значения"},
            {'data': '2022', 'answer': "2022 год пустой, заполните значения"},
            {'data': '2021', 'answer': "2021 год пустой, заполните значения"},
        )

        for item in items:
            with self.subTest(item['data']):
                self.base_url = '/calculate/' + item['data']
                output = self.app.get(self.base_url).data.decode()
                self.assertEqual(
                    output,
                    item['answer']
                )
