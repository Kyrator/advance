import unittest

from module_03_ci_culture_beginning.materials.previous_hw_test.hello_word_with_day import app


class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

