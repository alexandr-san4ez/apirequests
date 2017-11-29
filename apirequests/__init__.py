# -*- coding: UTF-8 -*-

"""
apirequests - implements a more convenient interface for constructing API to HTTP resources.

Built on `requests` and supports all its interfaces.
"""

import requests


class Client(requests.Session):
    """
    HTTP client for building API.

    Wrapper around the class :class:`requests.Session`.
    """

    #: Do not throw exceptions, by default throw out.
    silent = False

    def __init__(self, host):
        super(Client, self).__init__()

        #: The base address to the resource (hostname with paths
        #: for example 'http://example.com/api/').
        self.host = host.rstrip('/')

    def _url(self, path):
        """
        Returns the full path with the host name
        """
        return self.host + '/' + path.lstrip('/') if path else self.host

    def request(self, method, url, **kwargs):
        response = super(Client, self).request(method, self._url(url), **kwargs)

        if not self.silent:
            response.raise_for_status()

        return response
