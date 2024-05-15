#!/usr/bin/env python3
'''Simple module since it has a simple class.'''
import redis
import uuid
from typing import Union, Collable, Optional


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

    def get(key: str, fn: Optional[Collable] = None) -> Union[
            str, bytes, int, float]:
        """Gets and value from Redis data storage assiociated with key"""
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        """Retrieves a string value from a Redis data storage"""
        return self.get(key, lambda v: v.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieves an integer value from a Redis data storage"""
        return self.get(key, lambda v: int(v))
