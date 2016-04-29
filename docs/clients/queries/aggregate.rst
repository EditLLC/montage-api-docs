============
Aggregattion
============


Group
=====

Partition the documents into multiple groups based on the specified field

.. container:: example python

    .. code-block:: python

        Query('movies').group('year')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').group('year')


Count
=====

Count the number of documents in the sequence

.. container:: example python

    .. code-block:: python

        Query('movies').count()

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').count()


Sum
===

Sum the specified field of the sequence

.. container:: example python

    .. code-block:: python

        Query('movies').sum('rating')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').sum('rating')


Average
=======

Average the specified field of the sequence

.. container:: example python

    .. code-block:: python

        Query('movies').avg('rating')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').avg('rating')


Minimum
=======

Find the minimum value of the specified field in the sequence

.. container:: example python

    .. code-block:: python

        Query('movies').min('rating')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').min('rating')


Maximum
=======

Find the maximum value of the specified field of the sequence

.. container:: example python

    .. code-block:: python

        Query('movies').max('rating')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').max('rating')
