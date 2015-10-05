================
Query Descriptor
================

The query descriptor is a JSON object that defines the parameters for a query.

.. code::

    {
        "filter": {},
        "pluck": [],
        "without": [],
        "limit": null,
        "offset": null,
        "order_by": null,
        "ordering": "asc",
        "index": null,
        "batch_size": 1000,
    }


Parameters
==========

filter
------

Fetch documents that match the given lookup parameters.

The lookup parameters should be in the fomratdescribed in `Field Lookups`_
below. Multiple lookups will be effectively joined by ``AND``. Montage does not
(yet) support ``OR`` lookups.

Example::

    {"filter": {"author": "J.R.R. Tolkien", "genre": "Fantasy"}}

pluck
-----

Select one or more attributes from the result set. Only the attributes
specified will be returned in the results.

Example::

    {"pluck": ["title", "date_published", "author"]}

without
-------

The opposite of `pluck`_. Exclude one or more attributes from the result set.

Example::

    {"without": ["genre", "author"]}

limit
-----

End the result set after the specified number of documents.

Example::

    {"limit": 10}

offset
------

Skip the specified number of rows in the results. This is applied before
`limit`_.

Example::

    {"offset": 10}

order_by
--------

Order the results by a specific attribute. The default is no ordering.

Example::

    {"order_by": "date_published"}

ordering
--------

Order the documents in ascending (``asc``) or descending (``desc``) order. This
only works when `order_by`_ is also specified.

Example::

    {"order_by": "date_published", "ordering": "asc"}

index
-----

Manually choose which index to use for selecting the results.

Example::

    {"index": "date"}


Field Lookups
=============

Basic lookups
-------------

eq
~~

Example::

    {"field": value}

Equivalent::

    field == value

ieq
~~~

Case-insensitive version of `eq`_.

Example::

    {"field__ieq": value}

not
~~~

Example::

    {"field__not": value}

Equivalent::

    field != value

contains
~~~~~~~~

Example::

    {"field__contains": value}

Equivalent::

    value in field


icontains
~~~~~~~~~

Case-insensitive version of `contains`_.

Example::

    {"field__icontains": value}

in
~~

Example::

    {"field__in": value}

Equivalent::

    field in value

notin
~~~~~

Example::

    {"field__notin": value}

Equivalent::

    field not in value

gt
~~

Example::

    {"field__gt": value}

Equivalent::

    field > value

gte
~~~

Example::

    {"field__gte": value}

Equivalent::

    field >= value

lt
~~

Example::

    {"field__lt": value}

Equivalent::

    field < value

lte
~~~

Example::

    {"field__lte": value}

Equivalent::

    field <= value

startswith
~~~~~~~~~~

Example::

    {"field__startswith": value}

Equivalent::

    field.startswith(value)

istartswith
~~~~~~~~~~~

Case-insensitive version of `startswith`_.

Example::

    {"field__startswith": value}

endswith
~~~~~~~~

Example::

    {"field__endswith": value}

Equivalent::

    field.endswith(value)

iendswith
~~~~~~~~~

Case-insensitive version of `endswith`_.

Example::

    {"field__endswith": value}

regex
~~~~~

Example::

    {"field__regex": value}

Equivalent::

    field.match(value)

iregex
~~~~~~

Case-insensitive version of `regex`_.

Example::

    {"field__iregex": value}

Geospatial lookups
------------------

includes
~~~~~~~~

Example::

    {"field__includes": geojson}

Equivalent::

    field.includes(geojson)

intersects
~~~~~~~~~~

Example::

    {"field__includes": geojson}

Equivalent::

    field.includes(geojson)
