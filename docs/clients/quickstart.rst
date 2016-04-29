===============
Getting started
===============

Installation
============

.. container:: example python

    The Python library can be installed with pip.

    .. code-block:: bash

        pip install -e git+git://github.com/EditLLC/python-montage@master#egg=montage

.. container:: example javascript

    .. code-block:: bash

        npm install montage-data


Creating a client instance
==========================

.. container:: example python

    .. code-block:: python

        import montage
        client = montage.Client(subdomain)

.. container:: example javascript

    .. code-block:: javascript

        var montage = require('montagedata');
        var client = new montage.Client(subdomain);

    The Montage wrapper is asynchronous, and any method that makes an HTTP
    request to the Montage API returns a `Promise` that will be fulfilled
    when the request completes. Call `.then` on the promise to capture the
    response data.

    .. code-block:: javascript

        client.users.list().then(response => {
            console.log(response.data)
        });


Authentication
==============

Token auth
----------

Authenticate with a user- or project-level API token. The token is passed to
the initialization of the `Client`.

.. container:: example python

    .. code-block:: python

        client = montage.Client(subdomain, token)


.. container:: example javascript

    .. code-block:: javascript

        var client = new montage.Client(subdomain, token);


User credentials
----------------

Calling the `.authenticate()` method on a `Client` instance will authenticate
against the Montage API. The authentication endpoint returns the users API
token to be used in subsequent API requests.

**Credentials should not be stored in any way after the authentication process.**

.. container:: example python

    .. code-block:: python

        client.authenticate(email, password)

.. container:: example javascript

    .. code-block:: javascript

        var client = new montage.Client(subdomain);
        client.authenticate(email, password);


Anonymous requests
------------------

Clients are not required to authenticate with the API; any unauthenticated
request is treated as an anonymous user. As with authentucated users, anonymous
users may be assigned permissions, and can be granted access to specific API
requests.
