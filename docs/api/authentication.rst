==============
Authentication
==============


Get current user
================

.. http:get:: /api/v1/user/

    :reqheader Authorization: Access token to authorize the request


Authentication
==============

.. http:post:: /api/v1/user/

    :query username: User email address, supplied by the user
    :query password: Password, supplied by the user

    **Example Response**:

    .. sourcecode:: json

        {"data": {
            "full_name": "Joe User",
            "email": "user@example.com",
            "token": "59e1d663-f19c-4330-9008-4c33208c9671"
        }}
