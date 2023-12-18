"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""
import re
import unittest
from hw1_registration import app

class TestReg(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        app.config['TESING'] = True
        app.config['DEBUG'] = False
        app.config['SECRET_KEY'] = 'secretkey'

        cls.app = app.test_client()
        cls.base_url = '/registration'

    def test_registration_normal_data(self):
        data = {
            'email': 'test@test.ru',
            'phone': 89261010771,
            'name': 'Alex',
            'address': 'Moscow ul.Grishina 18',
            'index': 121354,
            'comment': 'call me before arrived'
        }
        response = self.app.post(self.base_url, data=data)
        print(response.data.decode())
        if re.match('\.@w*.\w*', response.data.decode()):
            print(response.data.decode())

    def test_registration_unnormal_data(self):
        data = {
            'email': 'testtest.ru',
            'phone': '89261010771',
            'name': 'Alex',
            'address': 'Moscow ul.Grishina 18',
            'index': 121354,
            'comment': 'call me before arrived'
        }
        response = self.app.post(self.base_url, data=data)
        print(response.data.decode())
        if re.match('\.@w*.\w*', response.data.decode()):
            print(response.data.decode())

    def test_registration_without_email(self):
        data = {

            'phone': 89261010771,
            'name': 'Alex',
            'address': 'Moscow ul.Grishina 18',
            'index': 121354,
            'comment': 'call me before arrived'
        }
        response = self.app.post(self.base_url, data=data)
        print(response.data.decode())
        if re.match('\.@w*.\w*', response.data.decode()):
            print(response.data.decode())


if __name__ == '__main__':
    unittest.main()
