# -*- coding: utf-8 -*-
""" This module contains the views of this application

Use Django 3.2 and more.
Use Django class-based view

#### TESTS
python manage.py test flatpage.tests.test_views

#### DOCUMENTATIONS
! For more informations about this app, consult the app README.md file

#### AUTHORS & COPYRIGHT
By : Guillaume Sadler
For : GRIMORDAL
Join us on grimordal.com

"""

# DJANGO IMPORTS
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.utils.translation import get_language

from .models import Flatpage as FlatpageData


class DefaultFlatPageView(View):
    """ Flatpage > Default Flatpage View """

    flatpage_name = None

    if flatpage_name is None:
        flatpage_name = "index"

    def get(self, request, *args, **kwargs):
        """ Flatpage get method """

        flatpage_template = 'flatpage/default/{}.html'.format(
            self.flatpage_name
        )

        flatpage_datas = FlatpageData.objects.translate(
            get_language()
        ).get(
            template_name=self.flatpage_name
        )

        context = {
            'meta_tags': flatpage_datas
        }

        return render(
            request,
            flatpage_template,
            context
        )
