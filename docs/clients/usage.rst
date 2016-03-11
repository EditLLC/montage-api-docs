===========
Basic usage
===========

Authentication
==============

Token auth
----------

Authenticate with a user- or project-level API token. The token is passed to
the initialization of the `Client`.

.. container:: example python

    .. code-block:: python

        client = montage.Client('<project>', '<api token>')

.. container:: example ruby

    .. code-block:: ruby

        # TODO

.. container:: example javascript

    .. code-block:: javascript

        var client = new montage.Client('<project>', '<api token>');


User credentials
----------------

Calling the `.authenticate()` method on a `Client` instance will authenticate
against the Montage API. The authentication endpoint returns the users API
token to be used in subsequent API requests.

**Credentials should not be stored in any way after the authentication process.**

.. container:: example python

    .. code-block:: python

        client.authenticate('<email>', '<password>')

.. container:: example ruby

    .. code-block:: ruby

        # TODO

.. container:: example javascript

    .. code-block:: javascript

        var client = new montage.Client('<project>');
        client.authenticate('<email>', '<password>');

Base API layer
==============

Schemas
-------

.. container:: example python

    .. code-block:: python

        >>> client.schemas.list()
        >>> client.schemas.get('movies')

.. container:: example ruby

    .. code-block:: ruby

        # TODO

.. container:: example javascript

    .. code-block:: javascript

        client.schemas.list().then(x => {console.log(x.data)});

Querying documents
------------------

.. container:: example python

    .. code-block:: python

        >>> query = montage.Query('movies')
        >>> query = query.filter(montage.Field('year') >= 2000)
        >>> query = query.limit(10)
        >>> query = query.order_by('rating')
        >>> montage.run(query=query)

.. container:: example ruby

    .. code-block:: ruby

        # TODO

.. container:: example javascript

    .. code-block:: javascript

        var query = new montage.Query();
        query = query.filter({author: 'Eric Clapton'});
        query = query.order('rating', 'desc');
        client.documents('songs', query).then(response => {
            console.log(response.data);
        });
