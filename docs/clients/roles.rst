=====
Roles
=====

List roles
==========

.. container:: example python

    .. code-block:: python

        client.roles.list()

.. container:: example javascript

    .. code-block:: javascript

        client.roles.list()


Create role
===========

.. container:: example python

    .. code-block:: python

        client.roles.create(name[, add_users])

.. container:: example javascript

    .. code-block:: javascript

        client.roles.create(name[, add_users])



Get role
========

.. container:: example python

    .. code-block:: python

        client.roles.get(role_name)

.. container:: example javascript

    .. code-block:: javascript

        client.roles.get(role_name)


Update role
=============

.. container:: example python

    .. code-block:: python

        client.roles.update(role_name[, name[, add_users[, remove_users]]])

.. container:: example javascript

    .. code-block:: javascript

        client.roles.get(role_name[, name[, add_users[, remove_users]]])


Remove role
===========

.. container:: example python

    .. code-block:: python

        client.roles.remove(role_name)

.. container:: example javascript

    .. code-block:: javascript

        client.roles.remove(role_name)
