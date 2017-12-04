# -*- coding: UTF-8 -*-

"""
apirequests - implements a more convenient interface for constructing API to HTTP resources.

Built on `requests` and supports all its interfaces.
"""

from urllib.parse import urljoin

import requests

class Client(requests.Session):
    """
    HTTP client for building API.

    Wrapper around the class :class:`requests.Session`.
    """

    #: Do not throw exceptions, by default throw out.
    silent = False

    #: Add a slash to the end of the URL or not.
    slash = False

    def __init__(self, host):
        super(Client, self).__init__()

        #: The base address to the resource (hostname with paths
        #: for example 'http://example.com/api/').
        self.host = host

    def _url(self, path):
        """
        Returns the full path with the host name
        """
        url = urljoin(self.host, path) if path else self.host

        if self.slash and not url.endswith('/'):
            url += '/'

        return url

    def request(self, method, url, **kwargs):
        response = super(Client, self).request(method, self._url(url), **kwargs)

        if not self.silent:
            response.raise_for_status()

        return response
