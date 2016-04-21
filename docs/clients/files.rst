=====
Files
=====


List files
==========

.. container:: example python

    .. code-block:: python

        client.files.list()


Save file
=========

.. container:: example python

    .. code-block:: python

        client.users.save(*files)

    Files are expected to be tuples of :code:`(file_name, contents)`.

    .. code-block:: python

        # Each of these are perfectly acceptible.
        client.files.save(('foo.txt', open('/path/to/foo.txt')))
        client.files.save(('foo.txt', StringIO('This is foo.txt')))
        client.files.save(('foo.txt', 'This is foo.txt'))


Get file
========

.. container:: example python

    .. code-block:: python

        client.files.get(file_id)


Remove file
===========

.. container:: example python

    .. code-block:: python

        client.files.remove(file_id)
