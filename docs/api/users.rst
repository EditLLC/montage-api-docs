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

    :reqheader Authorization: Access token to authorize the request


Get a single user
=================

.. http:get:: /api/v1/user/<int:user_id>/

    :reqheader Authorization: Access token to authorize the request


Update a user
=============

.. http:put:: /api/v1/user/<int:user_id>/

    :query full_name: Name (first + last)
    :query email: Email address
    :query password: Password

    :reqheader Authorization: Access token to authorize the request


.. http:patch:: /api/v1/user/<int:user_id>/

    :reqheader Authorization: Access token to authorize the request


Delete a user
=============

.. http:delete:: /api/v1/files/<user_id>/

    :reqheader Authorization: Access token to authorize the request
