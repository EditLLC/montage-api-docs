=======
Queries
=======

The Query object
================

Queries are created by instantiating a ``Query`` object and passing it to the
``.execute()`` method of an API client. The ``Query`` class takes a single
parameter, the name of the schema to be queried, and provides numerous methods
to filter, refine, and aggregate your results.

.. container:: example python

    .. code-block:: python

        from montage import Query, Field
        query = Query('movies').count()
        client.execute(query=query)

.. container:: example javascript

    .. code-block:: javascript

        import {Query, Field} from 'montagedata';
        query = new Query('movies').count()
        client.execute(query=query)


Query methods
=============

.. toctree::
    :maxdepth: 1

    select
    transform
    manipulate
    aggregate
    geospatial
