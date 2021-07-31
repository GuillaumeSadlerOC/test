# -*- coding: utf-8 -*-
""" This module contains the custom django command of User application

Use Django 3.2 and more.

#### TESTS

#### DOCUMENTATIONS
! For more informations about this app, consult the app README.md file

#### AUTHORS & COPYRIGHT
By : Guillaume Sadler
For : GRIMORDAL
Join us on grimordal.com

"""

# DJANGO IMPORTS
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    """ Flatpages > Personalized command """

    def handle(self, *args, **options):
        """ User > Handle """

        # Load fixtures
        call_command(
            'loaddata',
            'default-flatpages',
            app_label='flatpage'
        )
