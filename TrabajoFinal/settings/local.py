from .base import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'Foro',
        'Trusted_Connection':'yes',
        'HOST': 'localhost',
        'OPTIONS':{
            'driver':'SQL Server Native Client 11.0',
        }
    },
} 

