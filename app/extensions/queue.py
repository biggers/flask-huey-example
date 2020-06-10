# coding: utf-8

__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

from huey import RedisHuey
from pprint import pprint

_huey = None


def create_huey(config):
    """ """
    global _huey

    if _huey is not None:
        return _huey

    _storage_args = {
        'read_timeout': config.get('HUEY_STORAGE_READ_TIMEOUT', 1),
        'host': config.get('HUEY_HOST', None),
        'port': config.get('HUEY_PORT', None),
        'db': config.get('HUEY_DB', None),

        # OBSOLETE in H.v2, breaks consumer-workers! (in: redis/connection.py)
        # 'max_errors': config.get('HUEY_STORAGE_MAX_ERRORS', 1000),

        # BROKEN use-of! -- in huey/storage.py:379
        # 'url': config.get('HUEY_STORAGE_URL', None),
        # 'connection_pool': config.get('HUEY_STORAGE_CONNECTION_POOL', None),
        # 'connection_params': config.get('HUEY_STORAGE_CONN_PARAMS', None),
    }

    pprint(_storage_args)
    breakpoint()

    _huey = RedisHuey(
        name=config.get('HUEY_TASK_QUEUE_NAME', 'FLASK-HUEY-EXAMPLE'),
        result_store=config.get('HUEY_RESULT_STORE', False),
        events=config.get('HUEY_EVENTS', True),
        store_none=config.get('HUEY_STORE_NONE', False),
        always_eager=config.get('HUEY_ALWAYS_EAGER', False),
        store_errors=config.get('HUEY_STORE_ERRORS', True),
        blocking=config.get('HUEY_BLOCKING', False),
        **_storage_args
    )

    return _huey

