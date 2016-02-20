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

        client = montage.Client(
            project='<project>',
            token='<api token>'
        )

.. container:: example ruby

    .. code-block:: ruby

        # TODO

.. container:: example javascript

    .. code-block:: javascript

        var client = montage.Client({
            domain:'<project>',
            token:'<api token>'
        });


User credentials
----------------

Calling the `.authenticate()` method on a `Client` instance will authenticate
against the Montage API. The authentication endpoint returns the users API
token to be used in subsequent API requests.

**Credentials must not be stored in any way after the authentication process.**

.. container:: example python

    .. code-block:: python

        client.authenticate(email='...', password='...')

.. container:: example ruby

    .. code-block:: ruby

        # TODO

.. container:: example javascript

    .. code-block:: javascript

        var client = montage.Client({
            domain: '<project>',
            username: '...',
            password: '...'
        });
        client.auth();

Base API layer
==============

Schemas
-------

.. container:: example python

    .. code-block:: python

        schema = client.schema('...')
        schema.detail()

.. container:: example ruby

    .. code-block:: ruby

        # TODO

.. container:: example javascript

    .. code-block:: javascript

        client.schemas().then(x => {console.log(x.data)});
        client.schema('...');

Querying documents
------------------

.. container:: example python

    .. code-block:: python

        query = schema.documents.query()  # Effectively, fetch all
        query = query.filter(**kwargs)
        query = query.limit(0)
        query = query.offset(0)
        query = query.order(field[, ordering=asc|desc])
        for document in query:
            print document['id']

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
