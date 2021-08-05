#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method, store an instance of the
   Redis client as a private variable named _redis (using redis.Redis()) and
   flush the instance using flushdb
"""
import redis
import uuid
from typing import Union, Callable, Optional

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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """This method take a key string argument and an optional
           Callable argument named fn
        """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(keys)

    def get_str(self, data: str) -> str:
        """Most common return type across redis-py is bytes 
           rather than str. Depending to our requirement 
           we Convert the bytes to str
        """
        return self._redis.get(data).decode('utf-8')

    def get_int(self, data: str) -> str:
        """Convert bytes to int"""
        return int(self._redis.get(data))
