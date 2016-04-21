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

        client.roles.list().then(x => { console.log(x.data) });


Create role
===========

.. container:: example python

    .. code-block:: python

        client.roles.create(name[, add_users])

.. container:: example javascript

    .. code-block:: javascript

        client.roles.create(name[, add_users]).then(x => { console.log(x.data) });



Get role
========

.. container:: example python

    .. code-block:: python

        client.roles.get(role_name)

.. container:: example javascript

    .. code-block:: javascript

        client.roles.get(role_name).then(x => { console.log(x.data) });


Update role
=============

.. container:: example python

    .. code-block:: python

        client.roles.update(role_name[, name[, add_users[, remove_users]]])

.. container:: example javascript

    .. code-block:: javascript

        client.roles.get(role_name[, name[, add_users[, remove_users]]]).then(x => { console.log(x.data) });


Remove role
===========

.. container:: example python

    .. code-block:: python

        client.roles.remove(role_name)

.. container:: example javascript

    .. code-block:: javascript

        client.roles.remove(role_name).then(x => { console.log(x.data) });
