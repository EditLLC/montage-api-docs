=======
Schemas
=======

List schemas
============

.. container:: example python

    .. code-block:: python

        client.schemas.list()

.. container:: example javascript

    .. code-block:: javascript

        client.schemas.list().then(x => { console.log(x.data) });


Create schema
=============

.. container:: example python

    .. code-block:: python

        client.schemas.create(name, fields)

.. container:: example javascript

    .. code-block:: javascript

        client.schemas.create(name, fields).then(x => { console.log(x.data) });



Get schema
==========

.. container:: example python

    .. code-block:: python

        client.schemas.get(name)

.. container:: example javascript

    .. code-block:: javascript

        client.schemas.get(name).then(x => { console.log(x.data) });


Update schema
=============

.. container:: example python

    .. code-block:: python

        client.schemas.update(name)

.. container:: example javascript

    .. code-block:: javascript

        client.schemas.get(name).then(x => { console.log(x.data) });


Remove schema
=============

.. container:: example python

    .. code-block:: python

        client.schemas.remove(name)

.. container:: example javascript

    .. code-block:: javascript

        client.schemas.remove(name).then(x => { console.log(x.data) });
