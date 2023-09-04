Introduction to Django and URL Patterns
=======================================

Django is a high-level Python web framework that follows the "batteries-included" philosophy, providing everything needed to build web applications quickly and efficiently. In this document, we will introduce Django and explore how URL patterns (routes) work in Django applications.

1. What is Django?
------------------

Django is a web framework written in Python that encourages the development of clean, maintainable, and scalable web applications. It follows the Model-View-Controller (MVC) architectural pattern, but in Django, it is often referred to as the Model-View-Template (MVT) pattern.

Key features of Django:
~~~~~~~~~~~~~~~~~~~~~~~

- Robust ORM (Object-Relational Mapping) for database interactions.
- URL routing and view handling for request/response processing.
- Built-in authentication and admin interface for managing the application.
- Extensive support for forms, templates, and reusable components (apps).

2. URLs and URL Patterns
------------------------

In Django, the URL patterns define how incoming requests are mapped to specific views, which are Python functions or classes that handle the request and produce a response. The URL patterns act as a routing mechanism for your Django application.

URL patterns are defined in the `urls.py` file for each app in your Django project. The `urls.py` file maps URL patterns to view functions or classes.

Example of a basic URL pattern:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's say we have an app named "myapp" with a view function named `home` that handles the root URL ("/"):

In `myapp/views.py`:

.. code:: python

    from django.http import HttpResponse

    def home(request):
        return HttpResponse("Welcome to myapp!")

In `myapp/urls.py`:

.. code:: python

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
    ]

3. URL Parameters and Named Groups
----------------------------------

Django allows you to capture parts of the URL as parameters using named groups. These captured values can then be passed as arguments to the view function.

Example of using URL parameters:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's modify the `urls.py` file to include a dynamic URL pattern that captures a parameter named "username":

.. code:: python

    urlpatterns = [
        path('', views.home, name='home'),
        path('user/<str:username>/', views.user_profile, name='user_profile'),
    ]

In `myapp/views.py`:

.. code:: python

    from django.http import HttpResponse

    def user_profile(request, username):
        return HttpResponse(f"Welcome to the profile of {username}!")

4. Including URL Patterns from Other Apps
-----------------------------------------

Django allows you to include URL patterns from other apps into the main `urls.py` file of your project using the `include` function.

Example of including URL patterns:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the main `urls.py` file of your project:

.. code:: python

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('myapp/', include('myapp.urls')),
    ]


4. Enviromente Variables
----------------------------------

Create an .env file in the root of your project. There we will add our environment variables, remember to update the values with those of your project:

    SECRET_KEY=django-insecure-^prw$_z^2)+x0omx@d%p-toes4-+z+_kl(=$duc@qgi3^@8s*v
    DEBUG=True
    DB_NAME=tiendaonline
    DB_USER=postgres
    DB_PASSWORD=post123
    DB_HOST=localhost
    ALLOWED_HOSTS=127.0.0.1, localhost

In your .gitignore file add the following:

    .env

For our Django application to be able to read the values of the .env file we need the help of a library. At this case we'll use python decouple

-First let's install the library:

    pip install python-decouple

In your settings.py you import the library:

    from decouple import config

And to access a value defined in the .env file we do the following:

    SECRET_KEY = config("SECRET_KEY")

By default decouple brings the values in string format, but a Django project needs several types of values such as the following:

DEBUG expects a boolean value True or False.
ALLOWED_HOSTS expects a list of hosts.
EMAIL_PORT expects an integer.
For this we have the cast argument:

    # De string a booleano
    DEBUG = config("DEBUG", cast=bool)
    
    # De string a entero
    EMAIL_PORT = config('EMAIL_PORT', cast=int)
    
    # Forma 1: De string a lista
    ALLOWED_HOSTS = config(
        'ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')]
    )
    
    # Forma 2: De string a lista
    from decouple import Csv
    
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

You can add default values to be used in case they do not exist in the .env file with the default argument:

    DEBUG = config('DEBUG', default=True, cast=bool)
