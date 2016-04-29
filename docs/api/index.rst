========
REST API
========

API URL
=======

All API endpoints are mounted to the project domain, with a path prefixed by
an API version number. For example, if you want a list of all the schemas in
your Montage database, you would call::

    https://your-project.mntge.com/api/v1/schemas/


Payload
=======

All create and update endpoints (`POST`, `PUT`, and `PATCH` requests) expect a
JSON payload, not form-encoded values.


API Endpoints
=============

.. toctree::
    :maxdepth: 1

    authentication
    users
    roles
    policies
    schemas
    documents
    processing
    files
