# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'


config = dict(
    HUEY_STORAGE_READ_TIMEOUT=1,
    HUEY_STORAGE_MAX_ERRORS=1000,

    # ONE of the following should be defined to override the
    # default Redis connection:

    # Connection Pool object OR ...
    # HUEY_STORAGE_CONNECTION_POOL=redis.ConnectionPool(host='10.0.0.1', port=6379, db=0),
    # HUEY_STORAGE_CONNECTION_POOL=None,

    # OR url notation
    # HUEY_STORAGE_URL='redis://[:password]@localhost:9000/1',
    # HUEY_STORAGE_URL='unix://[:password]@/path/to/socket.sock?db=2',
    # HUEY_STORAGE_URL=None,

    # BROKEN, in huey/storage.py:379, RedisStorage
    # HUEY_STORAGE_URL='redis://127.0.0.1:6379/1',

    HUEY_HOST='127.0.0.1',
    HUEY_PORT=6379,
    HUEY_DB=1,

    HUEY_TASK_QUEUE_NAME='FLASK-HUEY-EXAMPLE',

    HUEY_ALWAYS_EAGER=False,
    HUEY_BLOCKING=False,
    HUEY_EVENTS=True,
    HUEY_RESULT_STORE=False,
    HUEY_STORE_ERRORS=True,
    HUEY_STORE_NONE=False,
)
