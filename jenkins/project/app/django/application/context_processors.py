# -*- coding: utf-8 -*-
""" This module contains the context processor of this application

Use Django 3.2 and more.

#### TESTS

#### DOCUMENTATIONS
! For more informations about this app, consult the app README.md file

#### AUTHORS & COPYRIGHT
By : Guillaume Sadler
For : GRIMORDAL
Join us on grimordal.com

"""

from django.conf import settings

def app_envs(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    
    APP_URL = '{}://{}'.format(
        request.scheme, 
        settings.APP_URL
    )
    
    return {
        'APP_URL': APP_URL,
    }
