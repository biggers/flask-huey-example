# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

import os


class Config(object):
    SECRET_KEY = 'b2ac76038b0958772c7981da84de0f43b4962721cd51fe09'

    _TRUTHS = set(['True', 'true', 1, 'T', 't', '1'])
    DEBUG = os.getenv("DEBUG", "F") in _TRUTHS

    DEBUG_TOOLBAR_ENABLED = DEBUG
    DEBUG_TB_INTERCEPT_REDIRECTS = DEBUG


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TOOLBAR_ENABLED = True

    MAIL_SERVER = os.environ.get('MAIL_SERVER', '127.0.0.1')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 1025))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "F") in Config._TRUTHS

    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'fred@flintstone')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD' 'yabba-dabba-do')

    MAIL_DEFAULT_SENDER = 'paul.cunningham@huey.example.com'


class StagingConfig(Config):
    pass


class TestingConfig(Config):
    pass
