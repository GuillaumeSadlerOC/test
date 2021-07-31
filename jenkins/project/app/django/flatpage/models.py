# -*- coding: utf-8 -*-
""" This module contains the models of this application

Use Django 3.2 and more.
Use Django ORM
Use PostgreSQL 2.2.x

#### MODELS MIGRATIONS
`python manage.py makemigrations` &
`python manage.py migrate`

#### TESTS
`python manage.py test flatpage.tests.test_models`

#### DOCUMENTATIONS
! For more informations about this app, consult the app README.md file

#### AUTHORS & COPYRIGHT
By : Guillaume Sadler
For : GRIMORDAL
Join us on grimordal.com

"""

# DJANGO IMPORTS
from django.db import models
from django.utils.translation import ugettext_lazy as _
from translations.models import Translatable

from seo.models import MetaTag

class Flatpage(Translatable, MetaTag):
    """ Flatpage > Model flatpage """

    template_name = models.CharField(
        _('flatpage template name'),
        max_length=100,
        unique=True,
        default=""
    )

    title = models.CharField(
        _('flatpage title'),
        max_length=100,
        unique=True
    )

    class TranslatableMeta:
        """ Flatpage > translatable meta """

        fields = [
            'title',
            'meta_title',
            'meta_description',
            'meta_keywords',
            'meta_og_title',
            'meta_og_description',
            'meta_twitter_card_title',
            'meta_twitter_card_description'
        ]

    def __str__(self):
        """ Flatpage """
        return self.title
