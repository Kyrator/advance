import unittest
from freezegun import freeze_time
import datetime

from module_03_ci_culture_beginning.homework.hw4.person import Person


class TestApp(unittest.TestCase):

    @freeze_time("2023-12-01")
    def test_get_age(self):
        items = (
            {'yob': 1985, 'output': 38},
            {'yob': 2023, 'output': 0},
            {'yob': 2045, 'output': -22},

        )
        for item in items:
            with self.subTest(item['yob']):
                output = Person.get_age(Person(name="test", year_of_birth=item['yob'], address="test"))
                self.assertEqual(
                    output,
                    item['output']
                )

    def test_get_name(self):
        items = (
            {'name': 'Nike', 'output': 'Nike'},
            {'name': 'Make', 'output': 'Make'},
            {'name': 'Sasha', 'output': 'Sasha'},
        )
        for item in items:
            with self.subTest(item['name']):
                output = Person.get_name(Person(name=item['name'], year_of_birth=1970, address="test"))
                self.assertEqual(
                    output,
                    item['output']
                )

    def test_set_name(self):
        items = (
            {'name': 123},
            {'name': {10: 1}},
        )
        for item in items:
            with self.subTest(item['name']):
                with self.assertRaises(TypeError):
                    Person.set_name(name=item['name'])

    def test_set_address(self):
        items = (
            {'name': 123},
            {'name': {10: 1}},
        )
        for item in items:
            with self.subTest(item['name']):
                with self.assertRaises(TypeError):
                    Person.set_address(address=item['name'])

    def test_get_address(self):
        items = (
            {'address': 'Moscow', 'output': 'Moscow'},
            {'address': 'Smolensk', 'output': 'Smolensk'},
            {'address': 'Vladivostok', 'output': 'Vladivostok'},
        )
        for item in items:
            with self.subTest(item['address']):
                output = Person.get_address(Person(name="test", year_of_birth=1970, address=item['address']))
                self.assertEqual(
                    output,
                    item['output']
                 )

    def test_is_homeless(self):
        items = (
            {'address': 'Moscow', 'output': False},
            {'address': '', 'output': True},
        )
        for item in items:
            with self.subTest(item['address']):
                output = Person.is_homeless(Person(name="test", year_of_birth=1970, address=item['address']))
                self.assertEqual(
                    output,
                    item['output']
                )