Data model for SatFlora
==================================

Introduction
------------

We will describe the data models used in the server side to be incorporated into the fronted side

1. Login
For the login we are using 2 api calls first to validate the user in firebase, and the second to get the user info.


.. code-block:: text

    POST firebase (using the firebase plugin for angular)
    Request Body:

.. code-block:: json

    {
        "email": "john@example.com",
        "password": "mypassword",
        "returnSecureToken": true
    }

.. code-block:: text

    Response Body (200 ok):

.. code-block:: json

    {
  "kind": "data",
  "localId": "data",
  "email": "john@example.com",
  "displayName": "",
  "idToken": "sessionID",
  "registered": true
}

After that, a get request must be performed to

.. code-block:: text

    GET api/v1/user/

.. code-block:: text

    Response Body (200 ok):

.. code-block:: json

    {"username":"ZxTY9T9mmpMXs37GGI5ljRuYw4m1"
    ,"email":"",
    "id":2,
    "first_name":"",
    "last_name":"",
    "profile":{"phone":"111111",
                "address":"calle 1 # 1-01",
                "picture":null,
                "birthdate":"2023-07-19",
                "sex":"MA"}
    }