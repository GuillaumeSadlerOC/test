# -*- coding: utf-8 -*-
""" This module is the app configuration of this application

Use Django 3.2 and more.

#### DOCUMENTATIONS
! For more informations about this app, consult the app README.md file

#### AUTHORS & COPYRIGHT
By : Guillaume Sadler
For : GRIMORDAL
Join us on grimordal.com

"""

# DJANGO IMPORTS
from django.apps import AppConfig


class FlatpageConfig(AppConfig):
    """ Flatpage config """

    name = 'flatpage'

    def ready(self):
        import flatpage.signals
