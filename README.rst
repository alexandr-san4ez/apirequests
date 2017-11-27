apirequests
===========

Implements a more convenient interface for constructing API to HTTP
resources.

Features
--------

-  The ability to specify a ``host`` and use relative links;
-  The choice between: checking the status of the response and raises
   exceptions (``silent`` parameter);
-  It is based on `requests`_ and supports all its interfaces;
-  is will be more...

Install
-------

``pip install apirequests``

Usage
-----

.. code:: python

    import apirequests

    class GitHub(apirequests.Client):
        silent = False
        def __init__(self):
            super(GitHub, self).__init__('https://api.github.com/')

    github = GitHub()
    print(github.get('zen').text)
    print(github.get('users/defunkt').json())

.. _requests: https://github.com/requests/requests