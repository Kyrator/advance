import unittest
from freezegun import freeze_time

from module_03_ci_culture_beginning.homework.hw1.hello_word_with_day import app


class TestApp(unittest.TestCase):
    def setUp(self):
        """Конфигурационная функция"""
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_name(self):
        """Проверка на отображение имени"""
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_cannot_get_correct_name(self):
        """Когда после имени стоит дополнительные символы"""
        username = 'username/asdjkllj'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertFalse(username in response_text)

    @freeze_time("2023-11-20")
    def test_can_get_monday(self):
        """Проверка на день недели понедельник"""
        username = 'username'
        day_week_monday = 'Хорошего понедельника'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(day_week_monday in response_text)

    @freeze_time("2023-11-21")
    def test_can_get_tuesday(self):
        """Проверка на день недели вторника"""
        username = 'username'
        day_week_tuesday = 'Хорошего вторника'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(day_week_tuesday in response_text)

    @freeze_time("2023-11-22")
    def test_can_get_wednesday(self):
        """Проверка на день недели среды"""
        username = 'username'
        day_week_wednesday = 'Хорошей среды'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(day_week_wednesday in response_text)

    @freeze_time("2023-11-23")
    def test_can_get_thursday(self):
        """Проверка на день недели четверга"""
        username = 'username'
        day_week_thursday = 'Хорошего четверга'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(day_week_thursday in response_text)

    @freeze_time("2023-11-24")
    def test_can_get_friday(self):
        """Проверка на день недели пятницы"""
        username = 'username'
        day_week_friday = 'Хорошей пятницы'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(day_week_friday in response_text)

    @freeze_time("2023-11-25")
    def test_can_get_saturday(self):
        """Проверка на день недели субботы"""
        username = 'username'
        day_week_saturday = 'Хорошей субботы'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(day_week_saturday in response_text)

    @freeze_time("2023-11-26")
    def test_can_get_sunday(self):
        """Проверка на день недели воскресенья"""
        username = 'username'
        day_week_sunday = 'Хорошего воскресенья'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(day_week_sunday in response_text)
