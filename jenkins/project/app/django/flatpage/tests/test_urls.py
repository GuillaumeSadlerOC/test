# -*- coding: utf-8 -*-
""" Urls test of Forum application

Use Django 3.2 and more.

#### DOCUMENTATIONS
! For more informations about this app, consult the app README.md file

#### AUTHORS & COPYRIGHT
By : Guillaume Sadler
For : GRIMORDAL
Join us on grimordal.com

"""

# DJANGO IMPORTS
from django.test import TestCase
from django.urls import resolve
from django.utils.translation import activate


class TestUrls(TestCase):
    """ Flatpages > Test urls """

    @classmethod
    def setUpTestData(cls):
        """ language activation """
        activate('fr')
    
    def test_index_url(self):
        """ Test """

        # URL
        resolver_match = resolve(
            '/fr/'
        )
        # Test view
        self.assertEqual(
            resolver_match.func.__name__,
            'DefaultFlatPageView'
        )
        # Test args
        self.assertEqual(
            resolver_match.args, ()
        )
        # Test kwargs
        self.assertEqual(
            resolver_match.kwargs, {}
        )
        # Test url name
        self.assertEqual(
            resolver_match.url_name,
            'index'
        )
        # Test route
        self.assertEqual(
            resolver_match.route,
            'fr/'
        )
        # Test app name
        self.assertEqual(
            resolver_match.app_name,
            'flatpage'
        )
        # Test namespace
        self.assertEqual(
            resolver_match.namespace,
            'flatpage'
        )
        # Test view name
        self.assertEqual(
            resolver_match.view_name,
            'flatpage:index'
        )
