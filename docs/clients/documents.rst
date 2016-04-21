=========
Documents
=========

List documents
==============

There is no document list endpoint. Instead, you should write a query to fetch
documents.


Save document
=============

.. container:: example python

    .. code-block:: python

        client.documents.create(name, fields)

.. container:: example javascript

    .. code-block:: javascript

        client.documents.create(name, fields).then(x => { console.log(x.data) });



Get document
============

.. container:: example python

    .. code-block:: python

        client.documents.get(schema_name, document_id)

.. container:: example javascript

    .. code-block:: javascript

        client.documents.get(schema_name, document_id).then(x => { console.log(x.data) });


Replace document
================

.. container:: example python

    .. code-block:: python

        client.documents.replace(schema_name, document)

.. container:: example javascript

    .. code-block:: javascript

        client.documents.replace(schema_name, document).then(x => { console.log(x.data) });


Update document
===============

.. container:: example python

    .. code-block:: python

        client.documents.update(schema_name, document_fragment)

.. container:: example javascript

    .. code-block:: javascript

        client.documents.update(schema_name, document_fragment).then(x => { console.log(x.data) });


Remove document
===============

.. container:: example python

    .. code-block:: python

        client.documents.remove(schema_name, document_id)

.. container:: example javascript

    .. code-block:: javascript

        client.documents.remove(schema_name, document_id).then(x => { console.log(x.data) });
