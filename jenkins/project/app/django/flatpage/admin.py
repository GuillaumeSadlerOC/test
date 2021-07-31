# -*- coding: utf-8 -*-
""" This module is the admin configuration of this application

Use Django 3.2 and more.

#### DOCUMENTATIONS
! For more informations about this app, consult the app README.md file

#### AUTHORS & COPYRIGHT
By : Guillaume Sadler
For : GRIMORDAL
Join us on grimordal.com

"""

# LIBRARY IMPORTS
from translations.admin import TranslatableAdmin, TranslationInline

# DJANGO IMPORTS
from django.contrib import admin

# CURRENT APP IMPORTS
from .models import Flatpage


class FlatpageAdmin(TranslatableAdmin):
    """ Flatpage > Flatpage admin """

    inlines = [TranslationInline]

admin.site.register(
    Flatpage,
    FlatpageAdmin
)
