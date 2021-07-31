# -*- coding: utf-8 -*-
""" This module contains the custom django command of User application

Use Django 3.x and more.

#### TESTS
python manage.py test user.tests.test_commands

#### DOCUMENTATIONS
! For more informations about this app, consult : user/README.md
Django custom command : https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/

#### MODIFICATIONS
Last modification date : 28/08/2019
By : Guillaume Sadler - https://github.com/TheodoraxX

"""

# DJANGO IMPORTS
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import Group

# CURRENT APP IMPORTS
from django.contrib.auth.models import User

class Command(BaseCommand):
    """ User > Personalized command """

    def handle(self, *args, **options):
        """ User > Handle """

    # Create Superuser
    super_user = User.objects.create_superuser(
        email='superuser@example.com',
        password='password@',
        username='root'
    )