import unittest

from flask import json

from application.app import app
from config import TestConfig


class TestTotal(unittest.TestCase):
    def setUp(self):
        self.test_app = app
        self.test_app.testing = True
        self.test_app.config.from_object(TestConfig)
        self.client = self.test_app.test_client()
        self.response = self.client.get('/total')

    def test_total_correct_return_value(self):
        expected = {'total': 3}

        resp_value = self.response.get_data()
        parsed_resp = json.loads(resp_value.decode())

        self.assertEqual(expected, parsed_resp)

    def test_total_success_response_code(self):
        resp_code = self.response.status_code

        self.assertEqual(200, resp_code)


if __name__ == '__main__':
    unittest.main()
