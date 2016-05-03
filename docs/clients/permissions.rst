===========
Permissions
===========

The policy document
===================

Permissions are defined by a set of policies. Policies are JSON documents that
describe what users can perform specific actions on certain resources.


Top-level keys
--------------


Policy documents have three required and one optional top-level keys.


``version``
~~~~~~~~~~~

Policy engine version identifier. This currently must be set to the
string ``v1``.


``grant``
~~~~~~~~~

A boolean that define whether the permission is granted or denied.


``statements``
~~~~~~~~~~~~~~

A list of objects that are used to match actions, resources, and users. If any
of the statements in a policy match, the


``action``

A list of actions that the user can perform on the specified resources


``resource``

The resource identifier that the user can


``principal``

Match anonymous users and/or registered users by ID, email, or role.

====================== ======================================= =======================================
Match by               Principal                               Example
====================== ======================================= =======================================
User ID                ``montage:user:id:{user.id}``           ``montage:user:id:4214``
Email                  ``montage:user:email:{user.email}``     ``montage:user:email:user@example.com``
Role                   ``montage:role:{role.name}``            ``montage:role:Admins``
Anonymous users        ``montage:user:anonymous``              ``montage:user:anonymous``
====================== ======================================= =======================================


``condition``
~~~~~~~~~~~~~

An object that specifies under what conditions a policy is applicable. If
conditions are unmet, the policy is ignored for that permissions check.

Optional.

.. code-block:: json

    {
        # ...
        "<condition>": {"<operator>": <value>}
    }


``request.ip``
^^^^^^^^^^^^^^

Match the IP address or network of the request. The value must be an array
of strings.

Supported operators: ``eq``, ``ne``

.. code-block:: javascript

    {
        # ...
        "condition": {
            "request.ip": {"eq": ["127.0.0.1", "98.224.0.0/32"]}
        }
    }

``request.host``
^^^^^^^^^^^^^^^^

Match the hostname of the request. The value must be an array of strings.

Supported operators: ``eq``, ``ne``

.. code-block:: javascript

    {
        # ...
        "condition": {
            "request.host": {"eq": ["domain.com", "*.domain.com"]}
        }
    }


``request.referer``
^^^^^^^^^^^^^^^^^^^

Match the HTTP referer (if any) of the request. The value must be an array
of strings.

Supported operators: ``eq``, ``ne``

.. code-block:: javascript

    {
        # ...
        "condition": {
            "request.referer": {"eq": ["https://domain.com/*"]}
        }
    }


``now.date``
^^^^^^^^^^^^

Supported operators: ``eq``, ``ne``, ``gt``, ``ge``, ``lt``, ``le``

.. code-block:: javascript

    {
        # ...
        "condition": {
            "now.date": {"gt": "2016-07-24"}
        }
    }


``now.time``
^^^^^^^^^^^^

Supported operators: ``eq``, ``ne``, ``gt``, ``ge``, ``lt``, ``le``

.. code-block:: javascript

    {
        # ...
        "condition": {
            "now.time": {"lt": "17:00"}
        }
    }


``now.datetime``
^^^^^^^^^^^^^^^^

Supported operators: ``eq``, ``ne``, ``gt``, ``ge``, ``lt``, ``le``

.. code-block:: javascript

    {
        # ...
        "condition": {
            "now.datetime": {"ge": "2016-07-24 20:07"}
        }
    }

Examples
--------

Grant any read action to all authenticated users:

.. code-block:: javascript

    {
        'version': 'v1',
        'grant': True,
        'statements': [
            {
                'action': [
                    'montage:*:list',
                    'montage:*:detail'
                ],
                'resource': '*',
                'principal': [
                    'montage:user:id:*'
                ],
            }
        ]
    }

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
