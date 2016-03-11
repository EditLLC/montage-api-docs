=========
Documents
=========


Create or update documents
==========================

.. http:post:: /api/v1/schemas/<str:schema>/documents/

    Batch create or update documents. The POST data must be one or many JSON
    objects that conform to the schema.

    :reqheader Authorization: Access token to authorize the request


Get a single document
=====================

.. http:get:: /api/v1/schemas/<str:schema>/documents/<uuid:document_id>/

    :reqheader Authorization: Access token to authorize the request


Update a document
=================

.. http:post:: /api/v1/schemas/<str:schema>/documents/<uuid:document_id>/

    :reqheader Authorization: Access token to authorize the request


Delete a document
=================

.. http:delete:: /api/v1/schemas/<str:schema>/documents/<uuid:document_id>/

    :reqheader Authorization: Access token to authorize the request
