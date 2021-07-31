# -*- coding: utf-8 -*-
""" This module is the app configuration of this application

Use Django 3.0.2 and more.

#### DOCUMENTATIONS
! For more informations about this app, consult the app README.md file

#### AUTHORS & COPYRIGHT
By : Guillaume Sadler
For : Greldas
Join us on www.greldas.com

"""


# DJANGO IMPORTS
from django.apps import AppConfig


class SEOConfig(AppConfig):
    """ SEOConfig config """

    name = 'seo'

    def ready(self):
        import seo.signals
