# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

from huey_config import config
from app.extensions.queue import create_huey

huey = create_huey(config)

import app.tasks


if __name__ == '__main__':
    pass
