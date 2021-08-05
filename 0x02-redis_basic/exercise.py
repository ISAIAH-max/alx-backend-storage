#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method, store an instance of the
   Redis client as a private variable named _redis (using redis.Redis()) and
   flush the instance using flushdb
"""
import redis
import uuid
from typing import Union

class Cache:
    """A redis cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method that takes a data argument and returns a string"""
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key
