import unittest
from remote_execution import app


class RemoteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        cls.app = app.test_client()
        cls.base_url = '/run_code'

    def test_timeout(self):
        """Тайм-аут ниже, чем время исполнения"""
        data = {
            'code': 'print([i*i*i for i in range(20000000)])',
            'timeout': 1,
        }
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(
            response.data.decode(),
            'Stdout: , stderr: , process was killed by timeout True'
        )

    def test_form_valid(self):
        """Некорректно введённые данные в форме."""
        data = {
            'code': 'print("Hello World!")',
            'timeout': 1,
        }
        response = self.app.post(self.base_url, data=data)
        self.assertRaises(
            TypeError
        )

    def test_shell_true(self):
        """Безопасный ввод в поле с кодом (проверка на `shell=True`)"""
        data = {
            'code': 'print()"; echo "hacked',
            'timeout': 3,
        }
        response = self.app.post(self.base_url, data=data)
        self.assertRaises(
            ValueError
        )


if __name__ == '__main__':
    unittest.main()
