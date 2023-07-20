Introduction to Django REST Framework
=====================================

Django REST Framework (DRF) is a powerful toolkit for building Web APIs in Django applications. It provides several core components that facilitate the development of robust and efficient APIs. In this document, we will explore essential concepts in DRF, including Views, ViewSets, Serializers, URLs, and Permissions.

1. Views and ViewSets
---------------------

In Django, a View is a function-based or class-based representation of a web page or API endpoint. A View processes an incoming HTTP request and returns an HTTP response. DRF extends the concept of Views with ViewSets, which group related operations for a resource into a single class. ViewSets reduce boilerplate code and improve code organization.

Usage of ViewSets
~~~~~~~~~~~~~~~~~

To use ViewSets, you need to define a serializer and a queryset for the resource. The serializer handles the conversion between complex Python data types and native data types, while the queryset defines the set of records from the database.

Example of a basic ViewSet:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's create a simple ViewSet for managing `Book` resources:

.. code:: python

    # serializers.py
    from rest_framework import serializers

    class BookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = '__all__'

    # views.py
    from rest_framework import viewsets
    from .models import Book
    from .serializers import BookSerializer

    class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer

2. Serializers
--------------

Serializers in Django REST Framework are similar to Django forms but designed to handle complex data types like JSON. Serializers convert complex data such as QuerySets and model instances to Python data types and then into JSON or XML representations for API responses.

Usage of Serializers
~~~~~~~~~~~~~~~~~~~~

To use serializers, define a serializer class that extends DRF's `serializers.Serializer` or `serializers.ModelSerializer`. The `ModelSerializer` class automatically generates serializers based on the model.

Example of a basic serializer:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's create a simple serializer for the `Book` model:

.. code:: python

    from rest_framework import serializers
    from .models import Book

    class BookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = '__all__'

3. Permissions
--------------

Permissions in Django REST Framework determine whether a user has permission to perform specific actions on resources. DRF provides various built-in permission classes, such as `IsAuthenticated`, `IsAdminUser`, `IsAuthenticatedOrReadOnly`, and more. You can also create custom permission classes to suit your application's needs.

Usage of Permissions
~~~~~~~~~~~~~~~~~~~~

To use permissions, set the `permission_classes` attribute on the ViewSet.

Example of applying permissions in django:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from rest_framework import permissions
    from .permissions import IsOwnerOrReadOnly

    class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

4. URLs and Routers
-------------------

In DRF, URLs map API endpoints to Views or ViewSets. URLs are defined in the `urls.py` file of your app. DRF provides a `DefaultRouter` that automatically generates URL patterns for ViewSets.

Usage of URLs and Routers
~~~~~~~~~~~~~~~~~~~~~~~~~

To use URLs and Routers, define URL patterns for your app's ViewSets and connect them to the main `urls.py` file.

Example of URL configuration:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In `views.py`:

.. code:: python

    from rest_framework.routers import DefaultRouter
    from .views import BookViewSet

    router = DefaultRouter()
    router.register(r'books', BookViewSet)

    urlpatterns = router.urls

5. API Root and Browsable API
-----------------------------

DRF provides a browsable API that allows developers to interact with the API using a web browser. The API root view displays a list of available endpoints.

Usage of API Root and Browsable API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable the browsable API and the API root view, include the `rest_framework.urls` in the main `urls.py` file:

.. code:: python

    from django.urls import path, include

    urlpatterns = [
        path('api/', include('myapp.urls')),
        path('api-auth/', include('rest_framework.urls')),
    ]
