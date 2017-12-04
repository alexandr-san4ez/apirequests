# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import patch

import requests

from apirequests import Client

class TestClient(unittest.TestCase):

    def test_init(self):
        c = Client('localhost')
        self.assertEqual('localhost', c.host)
        self.assertFalse(c.silent)
        self.assertFalse(c.slash)

    def test_url(self):
        localhost = 'http://localhost'
        c = Client(localhost)
        self.assertEqual(localhost + '/path', c._url('path'))
        self.assertEqual(localhost + '/path/23/', c._url('/path/23/'))

        c = Client(localhost + '/api/')
        self.assertEqual(localhost + '/api/path', c._url('path'))
        self.assertEqual(localhost + '/api/path/', c._url('path/'))
        self.assertEqual(localhost + '/abspath/', c._url('/abspath/'))

        c = Client(localhost)
        self.assertEqual(localhost + '/', c._url('/'))
        self.assertEqual(localhost, c._url(''))
        self.assertEqual(localhost, c._url(None))

        c = Client(localhost)
        c.slash = True
        self.assertEqual(localhost + '/', c._url(None))
        self.assertEqual(localhost + '/path/', c._url('path'))
        self.assertEqual(localhost + '/path/', c._url('/path/'))

    @patch('requests.Session.request')
    def test_request(self, request_mock):
        c = Client('http://localhost')

        c.request('GET', 'path', data=42)
        request_mock.assert_called_once_with('GET', 'http://localhost/path', data=42)

        response = requests.Response()
        request_mock.return_value = response

        c.silent = True
        response.status_code = 200
        self.assertTrue(c.request('GET', '/').ok)

        response.status_code = 500
        self.assertFalse(c.request('GET', '/').ok)

        c.silent = False
        response.status_code = 404
        with self.assertRaisesRegex(requests.exceptions.HTTPError, '404'):
            c.request('GET', '/')

        response.status_code = 200
        self.assertTrue(c.request('GET', '/').ok)


if __name__ == "__main__":
    unittest.main()
