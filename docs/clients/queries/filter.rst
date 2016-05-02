=========
Filtering
=========

The Field object
================

In order to express filters, you'll need to import ``Field``, in addition to
``Query``:

.. container:: example python

    .. code-block:: python

        from montage import Query, Field

.. container:: example javascript

    .. code-block:: javascript

        import {Query, Field} from 'montagedata';

Comparison filters
==================

.. container:: example python

    .. note::

        The Python library supports native syntax for comparison operations
        where possible. This syntax uses comparison operators directly instead
        of calling a method on ``Field``. Operators include ``==``, ``<``,
        ``>``, ``<=``, and ``>=``. Examples for both will be given when
        available.

Equal
-----

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('year') == 2009
        )

    .. code-block:: python

        Query('movies').filter(
            Field('year').eq(2009)
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('year').eq(2009)
        )

Case-insensitive equals
~~~~~~~~~~~~~~~~~~~~~~~

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('name').ieq('star wars')
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('name').ieq('star wars')
        )


Not equal
---------

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('year') != 2009
        )

    .. code-block:: python

        Query('movies').filter(
            Field('year').ne(2009)
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('year').ne(2009)
        )

Less than
---------

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('year') < 1990
        )

    .. code-block:: python

        Query('movies').filter(
            Field('year').lt(1990)
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('year').lt(1990)
        )

Less or equal
-------------

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('year') <= 1990
        )

    .. code-block:: python

        Query('movies').filter(
            Field('year').le(1990)
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('year').le(1990)
        )

Greater than
------------

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('year') > 2000
        )

    .. code-block:: python

        Query('movies').filter(
            Field('year').gt(2000)
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('year').gt(2000)
        )


Greater or equal
----------------

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('year') >= 2000
        )

    .. code-block:: python

        Query('movies').filter(
            Field('year').ge(2000)
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('year').ge(2000)
        )


In
--

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('year').in_([2000, 2001, 2002])
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('year').in([2000, 2001, 2002])
        )


Contains
--------

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('name').contains('the')
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('year').contains('the')
        )

Regular expression
------------------

Accepts `RE2 <https://github.com/google/re2>`_ syntax.

.. container:: example python

    .. code-block:: python

        Query('users').filter(
            Field('zipcode').regex('\d{5}')
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('user').filter(
            new Field('zipcode').regex('\d{5}')
        )


Starts with
-----------

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('name').starts('S')
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('name').starts('S')
        )

Case-insensitive starts with
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('name').istarts('s')
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('name').istarts('s')
        )

Ends with
---------

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('name').ends('W')
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('name').ends('W')
        )

Case-insensitive ends with
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('name').iends('w')
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('name').iends('w')
        )


Date and time filters
=====================



Date
----

.. container:: example python

    .. code-block:: python

        Query('games').filter(
            Field('timestamp').date() == '2016-02-17'
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('games').filter(
            new Field('timestamp').date().eq('2016-02-17')
        )

Time
----

.. container:: example python

    .. code-block:: python

        Query('games').filter(
            Field('timestamp').time() == '16:20'
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('games').filter(
            new Field('timestamp').time().eq('16:20')
        )

Year
----

.. container:: example python

    .. code-block:: python

        Query('users').filter(
            Field('birthday').year() == 1987
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('users').filter(
            new Field('birthday').year().eq(1987)
        )

Month
-----

.. container:: example python

    .. code-block:: python

        Query('users').filter(
            Field('birthday').month() == 7
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('users').filter(
            new Field('birthday').month().eq(7)
        )

Day
---

.. container:: example python

    .. code-block:: python

        Query('users').filter(
            Field('birthday').day() == 24
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('users').filter(
            new Field('birthday').day().eq(24)
        )

Hours
-----

.. container:: example python

    .. code-block:: python

        Query('games').filter(
            Field('timestamp').hours() == 12
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('games').filter(
            new Field('timestamp').hours().eq(12)
        )

Minutes
-------

.. container:: example python

    .. code-block:: python

        Query('games').filter(
            Field('timestamp').minutes() == 4
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('games').filter(
            new Field('timestamp').minutes().eq(4)
        )

Seconds
-------

.. container:: example python

    .. code-block:: python

        Query('games').filter(
            Field('timestamp').seconds() == 0
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('games').filter(
            new Field('timestamp').seconds().eq(0)
        )

Day of month
------------

.. container:: example python

    .. code-block:: python

        Query('games').filter(
            Field('timestamp').day_of_month() == 2
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('games').filter(
            new Field('timestamp').day_of_month().eq(2)
        )

Day of year
-----------

.. container:: example python

    .. code-block:: python

        Query('games').filter(
            Field('timestamp').day_of_year() == 52
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('games').filter(
            new Field('timestamp').day_of_year().eq(52)
        )


Geospatial filters
==================


Intersects
----------

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('location').intersects({
                'type': 'Polygon',
                'coordinates': [
                    [
                        [-119.92675781249999, 36.82357691815722],
                        [-119.7509765625, 36.6739263393281],
                        [-119.57382202148439, 36.80598611937673],
                        [-119.73724365234375, 36.914764288955936],
                        [-119.92675781249999, 36.82357691815722]
                    ]
                ]
            })
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('location').intersects({
                'type': 'Polygon',
                'coordinates': [
                    [
                        [-119.92675781249999, 36.82357691815722],
                        [-119.7509765625, 36.6739263393281],
                        [-119.57382202148439, 36.80598611937673],
                        [-119.73724365234375, 36.914764288955936],
                        [-119.92675781249999, 36.82357691815722]
                    ]
                ]
            })
        )

Includes
--------

.. container:: example python

    .. code-block:: python

        Query('movies').filter(
            Field('location').intersects({
                'type': 'Point',
                'coordinates': [-118.35399627685547, 34.13759651725404]
            })
        )

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').filter(
            new Field('location').intersects({
                'type': 'Point',
                'coordinates': [-118.35399627685547, 34.13759651725404]
            })
        )
