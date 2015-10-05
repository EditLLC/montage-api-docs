=========
Endpoints
=========

All API endpoints are mounted to the project domain::

    https://<project>.mntge.com

Authentication
==============

.. http:post:: /api/v1/auth/

    Retrieve a users access token, which is required for other endpoints.

    :query username: User email address, supplied by the user
    :query password: Password, supplied by the user

    **Example Response**:

    .. sourcecode:: json

        {"data": {"token": "59e1d663-f19c-4330-9008-4c33208c9671"}}

    The token must be sent in the headers of other endpoints which require it::

        Authorization: Token 59e1d663-f19c-4330-9008-4c33208c9671


.. http:get:: /api/v1/auth/user/

    Get the current users information

    :reqheader Authorization: Access token to authorize the request


Data
====

Schemas
-------

.. http:get:: /api/v1/schemas/

    Get a list of all schemas

    :reqheader Authorization: Access token to authorize the request


.. http:get:: /api/v1/schemas/<str:schema>/

    Get a single schema

    :reqheader Authorization: Access token to authorize the request


Documents
---------

.. http:get:: /api/v1/schemas/<str:schema>/query/

    Create a new query cursor and return the first batch of results OR
    get a batch of results for the specified cursor.

    :query query: A JSON-encoded query descriptor
    :query cursor: A cursor descriptor representing a batch of documents
        in a query results set.

    A GET request must include

    :reqheader Authorization: Access token to authorize the request


.. http:post:: /api/v1/schemas/<str:schema>/query/

    Create a new query cursor. POST data must be a JSON query that conforms to
    the **query** parameter of the GET method.

    :reqheader Authorization: Access token to authorize the request


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
