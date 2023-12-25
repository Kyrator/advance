import unittest
from unittest import TestCase
from redirect import Redirect


class TestRedirect(TestCase):
    def setUp(self):
        self.redirect = Redirect
        self.stdout_file = open('stdout.txt', 'w', encoding='UTF-8')
        self.stderr_file = open('stderr.txt', 'w', encoding='UTF-8')

    def test_redirect_stdout(self):
        pass
        # try:
        #     with self.redirect(stdout=self.stdout_file):
        #         print("Hello stdout.txt")
        # except Exception:
        #     pass
        # try:
        #     with open('stdout.txt', 'r') as file:
        #         read_file = file.read()
        # except Exception:
        #     pass
        #
        # self.assertEqual('Hello stdout.txt', read_file)

    def test_redirect_stderr(self):
        pass
        # with self.redirect(stderr=self.stderr_file):
        #     print("Hello stderr.txt")
        #     self.stderr_file.close()
        # with open('stderr.txt', 'r') as file:
        #     read_file = file.read()
        #     file.close()
        # self.assertEquals('Hello stdout.txt', read_file)


if __name__ == '__main__':
    unittest.main()
    with open('test_results.txt', 'a') as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)
