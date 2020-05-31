import os
import sys
import unittest
import requests
from unittest import TestCase


import datetime_service as ds


class TestDatetimeAPI(TestCase):

    def test_test_api(self):

        data = requests.get("http://0.0.0.0:5000/")
        self.assertEqual(data.status_code, 200)


if __name__ == '__main__':
    unittest.main()
