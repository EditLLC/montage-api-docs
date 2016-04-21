=====
Users
=====


Current user information
========================

.. container:: example python

    .. code-block:: python

        client.user()


Create a user
=============

.. container:: example python

    .. code-block:: python

        client.users.create(email, name, password)


List users
==========

.. container:: example python

    .. code-block:: python

        client.users.list()


Get user
========

.. container:: example python

    .. code-block:: python

        client.users.get(user_id)


Update user
===========

.. container:: example python

    .. code-block:: python

        client.users.update(user_id[, full_name[, email[, password]]])


Remove user
===========

.. container:: example python

    .. code-block:: python

        client.users.remove(user_id)
