=====
Roles
=====

List all roles
==============

.. http:get:: /api/v1/roles/


Create a new role
=================

.. http:post:: /api/v1/roles/

    :query name: Role name
    :query add_users: List of user IDs to add to the role


Get a single role
=================

.. http:get:: /api/v1/roles/<str:name>/


Update a role
=============

.. http:put:: /api/v1/roles/<str:name>/

    :query name: Role name
    :query add_users: List of user IDs to add to the role
    :query remove_users: List of user IDs to remove from the role


.. http:patch:: /api/v1/roles/<str:name>/


Delete a role
=============

.. http:delete:: /api/v1/roles/<str:name>/
