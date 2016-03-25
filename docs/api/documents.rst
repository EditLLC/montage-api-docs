=========
Documents
=========


Create or update documents
==========================

.. http:post:: /api/v1/schemas/<str:schema>/documents/

    Batch create or update documents. The POST data must be one or many JSON
    objects that conform to the schema.


Get a single document
=====================

.. http:get:: /api/v1/schemas/<str:schema>/documents/<uuid:document_id>/


Update a document
=================

.. http:put:: /api/v1/schemas/<str:schema>/documents/<uuid:document_id>/

.. http:patch:: /api/v1/schemas/<str:schema>/documents/<uuid:document_id>/


Delete a document
=================

.. http:delete:: /api/v1/schemas/<str:schema>/documents/<uuid:document_id>/
