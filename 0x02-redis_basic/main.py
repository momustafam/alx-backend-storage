#!/usr/bin/env python3
"""
Main file
"""
import redis
from exercise import replay
Cache = __import__('exercise').Cache

cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
