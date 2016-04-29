==============
Selecting data
==============

Get
===

Get a single document by its primary key

.. container:: example python

    .. code-block:: python

        Query('movies').get('08d56946-372d-4e7f-b227-157f6d70f84f')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').get('08d56946-372d-4e7f-b227-157f6d70f84f')


Get all
=======

Get all documents where the given value matches the requested index

.. container:: example python

    .. code-block:: python

        Query('movies').get_all(
            '08d56946-372d-4e7f-b227-157f6d70f84f',
            '8a1c7d43-419c-4ee7-81f4-47f7c7583f9e'
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').getAll(
            '08d56946-372d-4e7f-b227-157f6d70f84f',
            '8a1c7d43-419c-4ee7-81f4-47f7c7583f9e'
        )


Filter
======

Get all the documents for which the specified sequence is true

.. toctree::
    :hidden:
    :maxdepth: 1

    filter

.. container:: example python

    .. code-block:: python

        query = Query('movies').filter(
            Field('year') >= 1990,
            Field('year') <= 2000,
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').getAll(
            new Field('year').gt(1990),
            new Field('year').lt(2000),
        )

For more informations, see :doc:`filter`.

Between
=======

Get all the documents where the specified index falls between two values.

.. container:: example python

    .. code-block:: python

        query = Query('movies').between(1990, 2000, 'year')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').between(1990, 2000, 'year')
