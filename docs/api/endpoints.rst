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



Running scripts and queries
===========================


.. http:get:: /api/v1/query/

    Perform a data query, run a committed script, or run arbitrary Lua code.

    :reqheader Authorization: Access token to authorize the request

