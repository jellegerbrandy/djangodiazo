djangodiazo
===========

Integrate Diazo with Django

A very light wrapper around that applies DiazoMiddleware WSGI class the the django application


Installation
-------------

In your settings.py set:

WSGI_APPLICATION = 'djangodiazo.wsgi.application'

DIAZO_CONFIG = {
    'rules': 'path/to/your/rules.xml', 
}


Configuration Options
----------------------

All configuration options of DiazoMiddleware are supported. 

Documentation is here: http://docs.diazo.org/en/latest/deployment.html



