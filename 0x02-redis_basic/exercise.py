#!/usr/bin/env python3
'''Simple module since it has a simple class.'''
import redis
import uuid
from typing import Union


class Cache:
    '''Simple class that trying to cach some clients data.'''

    def __init__(self):
        '''Instantiate an object of Cache class.'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Store the input data in Redis.'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
