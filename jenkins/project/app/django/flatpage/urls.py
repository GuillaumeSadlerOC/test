# -*- coding: utf-8 -*-
""" This module is the URL dispatcher of this application

Go to application/urls.py for the main URL dispatcher.

Use Django 3.2 and more.

#### TESTS
python manage.py test flatpage.tests.test_urls

#### DOCUMENTATIONS
! For more informations about this app, consult the app README.md file

#### AUTHORS & COPYRIGHT
By : Guillaume Sadler
For : GRIMORDAL
Join us on grimordal.com

"""

# DJANGO IMPORTS
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _

# APP IMPORTS
from .views import DefaultFlatPageView

app_name = 'flatpage'

urlpatterns = [
    # Index
    path(
        '',
        DefaultFlatPageView.as_view(
            flatpage_name='index'
        ),
        name='index'
    ),
    # Cookies
    path(
        _('cookies'),
        DefaultFlatPageView.as_view(
            flatpage_name='cookies'
        ),
        name='cookies'
    ),
    # Credits
    path(
        _('credits'),
        DefaultFlatPageView.as_view(
            flatpage_name='credits'
        ),
        name='credits'
    ),
    # General Condition of Sale
    path(
        _('gcs'),
        DefaultFlatPageView.as_view(
            flatpage_name='gcs'
        ),
        name='gcs'
    ),
    # Legal Notice
    path(
        _('legal-notice'),
        DefaultFlatPageView.as_view(
            flatpage_name='legal-notice'
        ),
        name='legal-notice'
    ),
    # Privacy Policy
    path(
        _('privacy-policy'),
        DefaultFlatPageView.as_view(
            flatpage_name='privacy-policy'
        ),
        name='privacy-policy'
    ),
    # Therms and Conditions of Use
    path(
        _('tcu'),
        DefaultFlatPageView.as_view(
            flatpage_name='tcu'
        ),
        name='tcu'
    ),
]
