=====
Users
=====

List all users
==============

.. http:get:: /api/v1/users/


Create a new user
=================

.. http:post:: /api/v1/users/

    :query full_name: Name (first + last)
    :query email: Email address
    :query password: Password


Get a single user
=================

.. http:get:: /api/v1/user/<int:user_id>/


Update a user
=============

.. http:put:: /api/v1/user/<int:user_id>/

    :query full_name: Name (first + last)
    :query email: Email address
    :query password: Password


.. http:patch:: /api/v1/user/<int:user_id>/


Delete a user
=============

.. http:delete:: /api/v1/users/<int:user_id>/
