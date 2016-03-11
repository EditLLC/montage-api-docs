=====
Files
=====


List all files
==============

.. http:get:: /api/v1/files/

    :reqheader Authorization: Access token to authorize the request


Upload a file
=============

.. http:post:: /api/v1/files/

    :query file: One or more uploaded files
    :reqheader Authorization: Access token to authorize the request


Get a file
==========

.. http:get:: /api/v1/files/<uuid:file_id>/

    :reqheader Authorization: Access token to authorize the request


Delete a file
=============

.. http:delete:: /api/v1/files/<uuid:file_id>/

    :reqheader Authorization: Access token to authorize the request
