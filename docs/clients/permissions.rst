===================
Permission policies
===================

List policies
=============

.. container:: example python

    .. code-block:: python

        client.policies.list()

.. container:: example javascript

    .. code-block:: javascript

        client.policies.list()


Create policy
=============

.. container:: example python

    .. code-block:: python

        client.policies.create(description, policy)

.. container:: example javascript

    .. code-block:: javascript

        client.policies.create(description, policy)



Get policy
==========

.. container:: example python

    .. code-block:: python

        client.policies.get(policy_id)

.. container:: example javascript

    .. code-block:: javascript

        client.policies.get(policy_id)


Update policy
=============

.. container:: example python

    .. code-block:: python

        client.policies.update([description[, policy]])

.. container:: example javascript

    .. code-block:: javascript

        client.policies.update([description[, policy]])


Remove policy
=============

.. container:: example python

    .. code-block:: python

        client.policies.remove(policy_id)

.. container:: example javascript

    .. code-block:: javascript

        client.policies.remove(policy_id)
