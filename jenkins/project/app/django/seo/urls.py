# -*- coding: utf-8 -*-
""" This module is the URL dispatcher of this application

Go to application/urls.py for the main URL dispatcher.

Use Django 3.0.2 and more.

#### TESTS
python manage.py test auth.tests.test_urls

#### DOCUMENTATIONS
! For more informations about this app, consult the app README.md file

#### AUTHORS & COPYRIGHT
By : Guillaume Sadler
For : Greldas
Join us on www.greldas.com

"""

# DJANGO IMPORTS
from django.urls import path
from django.contrib.auth.decorators import login_required

# CURRENT APP IMPORTS

app_name = 'seo'

urlpatterns = [
]
