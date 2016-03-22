=====
Files
=====


List all files
==============

.. http:get:: /api/v1/files/


Upload a file
=============

.. http:post:: /api/v1/files/

    :query file: One or more uploaded files


Get a file
==========

.. http:get:: /api/v1/files/<uuid:file_id>/


Delete a file
=============

.. http:delete:: /api/v1/files/<uuid:file_id>/
