#file to config all default secret details (like aws, DB keys etc...)
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    DB_KEY = "123456"

class DevelopmentConfig(object):
    DEBUG = False
    DB_KEY = "123456"

class LocalConfig(object):
    DEBUG = False
    DB_KEY = "123456"


# like this we can create classes for stage and prod env.