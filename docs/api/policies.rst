========
Policies
========

List all policies
=================

.. http:get:: /api/v1/policy/


Create a new policy
===================

.. http:post:: /api/v1/policy/

    :query description: A short, one-line description of the policy
    :query policy: Policy document as JSON


Get a single policy
===================

.. http:get:: /api/v1/policy/<uuid:policy_id>/


Update a policy
===============

.. http:put:: /api/v1/policy/<uuid:policy_id>/

    :query name: Role name
    :query add_users: List of user IDs to add to the role
    :query remove_users: List of user IDs to remove from the role


.. http:patch:: /api/v1/policy/<uuid:policy_id>/


Delete a policy
===============

.. http:delete:: /api/v1/policy/<uuid:policy_id>/


Check permissions
=================

.. http:get:: /api/v1/policy/check/

    :query action: Action
    :query resource: Resource
