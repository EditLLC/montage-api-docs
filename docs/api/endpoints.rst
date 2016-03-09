=========
Endpoints
=========

All API endpoints are mounted to the project domain::

    https://<project>.mntge.com


Authentication
==============

.. http:get:: /api/v1/user/

    Get the current users information

    :reqheader Authorization: Access token to authorize the request


.. http:post:: /api/v1/user/

    Retrieve a users access token, which is required for other endpoints.

    :query username: User email address, supplied by the user
    :query password: Password, supplied by the user

    **Example Response**:

    .. sourcecode:: json

        {"data": {"token": "59e1d663-f19c-4330-9008-4c33208c9671"}}

    The token must be sent in the headers of other endpoints which require it::

        Authorization: Token 59e1d663-f19c-4330-9008-4c33208c9671


Users
=====


.. http:get:: /api/v1/users/

    List all users.


.. http:post:: /api/v1/users/

    Create a new user

    :query full_name: Name (first + last)
    :query email: Email address
    :query password: Password


.. http:get:: /api/v1/user/<int:user_id>/

    Retrieve the information for a single user.


.. http:put:: /api/v1/user/<int:user_id>/

    Update the information for a single user.


.. http:patch:: /api/v1/user/<int:user_id>/

    Partially update the information for a single user.


.. http:delete:: /api/v1/files/<user_id>/

    Delete a user



Running scripts and queries
===========================


.. http:get:: /api/v1/query/

    Perform a data query, run a committed script, or run arbitrary Lua code.

    :reqheader Authorization: Access token to authorize the request


Schemas
=======


.. http:get:: /api/v1/schemas/

    Get a list of all schemas

    :reqheader Authorization: Access token to authorize the request


.. http:get:: /api/v1/schemas/<str:schema>/

    Get a single schema

    :reqheader Authorization: Access token to authorize the request


Documents
=========


.. http:post:: /api/v1/schemas/<str:schema>/save/

    Batch create or update documents. The POST data must be one or many JSON
    objects that conform to the schema.

    :reqheader Authorization: Access token to authorize the request


.. http:get:: /api/v1/schemas/<str:schema>/<uuid:document_id>/

    Get the specified document.

    :reqheader Authorization: Access token to authorize the request


.. http:post:: /api/v1/schemas/<str:schema>/<uuid:document_id>/

    Replace the specified document. POST data must be a JSON document that
    conforms to the schema.

    :reqheader Authorization: Access token to authorize the request


.. http:delete:: /api/v1/schemas/<str:schema>/<uuid:document_id>/

    Delete a document.

    :reqheader Authorization: Access token to authorize the request


Files
=====

.. http:get:: /api/v1/files/

    List all files.


.. http:post:: /api/v1/files/

    Upload one or more files.

    :query file: One or more uploaded files


.. http:get:: /api/v1/files/<uuid:file_id>/

    Retrieve the information for a single file.


.. http:delete:: /api/v1/files/<uuid:file_id>/

    Delete a file
