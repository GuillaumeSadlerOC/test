# -*- coding: utf-8 -*-
""" This module contains the models of this application

Use Django 3.0.2 and more.
Use Django ORM
Use PostgreSQL 2.2.x

#### DATABASE SETTINGS
application/settings/dev.py
application/settings/preprod.py
application/settings/prod.py
application/settings/travis.py

#### MODELS MIGRATIONS
`python manage.py makemigrations` &
`python manage.py migrate`

#### TESTS
`python manage.py test flatpages.tests.test_models`

#### DOCUMENTATIONS
! For more informations about this app, consult the app README.md file

#### AUTHORS & COPYRIGHT
By : Guillaume Sadler
For : Greldas
Join us on www.greldas.com

"""

## DJANGO IMPORTS ##
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
## DJANGO MODULES IMPORTS ##
from translations.models import Translatable


class MetaTag(models.Model):
    """ """

    meta_title = models.CharField(
        _('meta title'),
        help_text=_("Required, max 65 caracters, must be unique"),
        unique=True,
        max_length=65,
        default=""
    )

    meta_description = models.CharField(
        _('meta description'),
        max_length=160,
        help_text=_("Required, max 160 caracters, must be unique"),
        unique=True,
        default=""
    )

    meta_keywords = models.CharField(
        _('meta keywords'),
        max_length=255,
        help_text=_("Optionnal, max 255 caracters"),
        null=True,
        blank=True,
        default=""
    )

    meta_robots = models.CharField(
        _('meta robots'),
        help_text=_("Required, NOODP, Index/Noindex, Follow/Nofollow, Nosnippet, Noarchive, Noimageindex"),
        max_length=100,
        blank=True,
        default='NOODP, Index, Follow'
    )

    image_src = models.ImageField(
        _('image source'),
        help_text=_(""),
        null=True,
        blank=True,
        upload_to='files/images/flatpages/'
    )

    ## META OG ##
    meta_og_title = models.CharField(
        _('meta og title'),
        help_text=_("Optionnal, content title, max 65 caracters, must be unique"),
        null=True,
        blank=True,
        max_length=100
    )

    meta_og_type = models.CharField(
        _('meta og type'),
        help_text=_("Optionnal, content type, https://ogp.me/#types"),
        null=True,
        blank=True,
        max_length=100,
        default="website"
    )

    meta_og_description = models.CharField(
        _('meta og description'),
        help_text=_("Optionnal, content description, max 200 caracters"),
        null=True,
        blank=True,
        max_length=200
    )

    meta_og_url = models.CharField(
        _('meta og url'),
        help_text=_("Optionnal, canonical url"),
        null=True,
        blank=True,
        max_length=255
    )

    ### META OG > IMAGE ###
    meta_og_image = models.ImageField(
        _('meta og image'),
        help_text=_("Optionnal, content image source, max image size : 1200x627 (px), max image size : 5MB "),
        null=True,
        blank=True,
        upload_to='files/images/flatpages/'
    )

    META_OG_IMAGE_TYPE = (
        ("image/jpeg", "image/jpeg"),
        ("image/gif", "image/gif"),
        ("image/png", "image/png")
    )

    meta_og_image_type = models.CharField(
        _('meta og image type'),
        help_text=_("Optionnal, image type"),
        max_length=100,
        choices=META_OG_IMAGE_TYPE,
        default=1
    )

    meta_og_image_width = models.PositiveIntegerField(
        _('meta og image width'),
        help_text=_("Optionnal, image width (pixel only)"),
        null=True,
        blank=True
    )

    meta_og_image_height = models.PositiveIntegerField(
        _('meta og image height'),
        help_text=_("Optionnal, image height (pixel only)"),
        null=True,
        blank=True
    )

    meta_og_image_alt = models.CharField(
        _('meta og alt'),
        help_text=_("Optionnal, alternative image text, max 100 caracters"),
        null=True,
        blank=True,
        max_length=100
    )

    ## TWITTER ##

    META_TWITTER_CARD_TYPE = (
        ("summary", "summary"),
        ("summary_large_image", "summary_large_image"),
        ("app", "app"),
        ("player", "player")
    )

    meta_twitter_card_type = models.CharField(
        _('meta twitter card type'),
        help_text=_("Optionnal, twitter card type"),
        max_length=100,
        choices=META_TWITTER_CARD_TYPE,
        default=1
    )

    meta_twitter_card_site = models.CharField(
        _('meta twitter card site'),
        help_text=_("Optionnal, twitter @username for the website used in the card footer, max 100 caracters"),
        null=True,
        blank=True,
        max_length=100
    )

    meta_twitter_card_creator = models.CharField(
        _('meta twitter card creator'),
        help_text=_("Optionnal, twitter @username for the content creator / author, max 100 caracters"),
        null=True,
        blank=True,
        max_length=100
    )

    meta_twitter_card_title = models.CharField(
        _('twitter card title'),
        help_text=_("Optionnal, a concise title for the related content, max 55 caracters"),
        null=True,
        blank=True,
        max_length=55
    )

    meta_twitter_card_description = models.CharField(
        _('twitter card description'),
        help_text=_("Optionnal, a concise description for the related content, max 125 caracters"),
        null=True,
        blank=True,
        max_length=125
    )

    meta_twitter_card_image = models.ImageField(
        _('twitter card image'),
        help_text=_("Optionnal, related content image, size : min 144x144(px)/300x157(px) & max 4096x4096(px), 5MB, type: JPG, PNG, WEBP, GIF "),
        null=True,
        blank=True,
        upload_to='files/images/flatpages/'
    )

    meta_twitter_card_image_alt = models.CharField(
        _('twitter card image alt'),
        help_text=_("Optionnal, alternative image text, max 100 caracters"),
        null=True,
        blank=True,
        max_length=100
    )

    ## I18N ##
    alternate_fr = models.CharField(
        _('alternate fr'),
        null=True,
        blank=True,
        default="",
        max_length=100
    )

    alternate_en = models.CharField(
        _('alternate en'),
        null=True,
        blank=True,
        default="",
        max_length=100
    )

    class Meta:
        abstract = True

    def __str__(self):
        """ Flatpage """
        return self.title
