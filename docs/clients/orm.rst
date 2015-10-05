===========
Model layer
===========

Montage provides an ActiveRecord-style ORM for working with data as objects
that can implement additional functionality.

Model syntax
============

.. container:: example python

    .. code-block:: python

        class User(montage.Model('users')):
            @property
            def full_name(self):
                return '{0} {1}'.format(self.first_name, self.last_name)

.. container:: example ruby

    .. code-block:: ruby

        # TODO

.. container:: example javascript

    .. code-block:: javascript

        // TODO

Querying
========

.. container:: example python

    .. code-block:: python

        albums = User.documents.get(username='deeps')

.. container:: example ruby

    .. code-block:: ruby

        # TODO

.. container:: example javascript

    .. code-block:: javascript

        // TODO

Model instances
===============

.. container:: example python

    .. code-block:: python

        album = Album.documents.filter(
            artist='Black Sabbath',
            name='Sbotage'
        )[0]
        album.name = 'Sabotage'
        album.save()
        album.delete()


.. container:: example ruby

    .. code-block:: ruby

        # TODO

.. container:: example javascript

    .. code-block:: javascript

        // TODO
