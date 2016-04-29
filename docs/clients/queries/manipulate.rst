============
Manipulation
============


Pluck
=====

Return only the specified fields

.. container:: example python

    .. code-block:: python

        Query('movies').pluck('id', 'name', 'year', 'rank')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').pluck('id', 'name', 'year', 'rank')

Without
=======

The opposite of pluck, return the documents without the specified fields

.. container:: example python

    .. code-block:: python

        Query('movies').without('rank', 'rating')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').without('rank', 'rating')
