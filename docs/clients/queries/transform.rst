==============
Transformation
==============


With fields
===========

Exclude documents that do not have the specified fields and return only those fields.

.. container:: example python

    Functionally, this is identical to ``has_fields`` followed by ``pluck``.

    .. code-block:: python

        Query('movies').with_fields('name', 'year', 'rating')

.. container:: example javascript

    Functionally, this is identical to ``hasFields`` followed by ``pluck``.

    .. code-block:: javascript

        new Query('movies').withFields('name', 'year', 'rating')


Has fields
==========

Test if a document has the specified fields, filtering out any that do not.

.. container:: example python

    .. code-block:: python

        Query('movies').has_fields('name', 'year', 'rating')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').hasFields('name', 'year', 'rating')


Order by
========

Sort the documents by the specified field.

.. container:: example python

    .. code-block:: python

        Query('movies').order_by('year')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').orderBy('year')


Skip
====

Skip a number of documents from the head of the sequence

.. container:: example python

    .. code-block:: python

        Query('movies').skip(5)

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').skip(5)


Limit
=====

End the sequence after the givin number of documents

.. container:: example python

    .. code-block:: python

        Query('movies').limit(10)

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').limit(10)


Slice
=====

Return the documents within the specified range

.. container:: example python

    .. code-block:: python

        Query('movies').slice(5, 15)

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').slice(5, 15)


Nth
===

Get the ``nth`` document in the sequence

.. container:: example python

    .. code-block:: python

        Query('movies').nth(7)

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').nth(7)


Sample
======

Select a given number of elements from a sequence with uniform random distribution

.. container:: example python

    .. code-block:: python

        Query('movies').sample(10)

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').sample(10)
