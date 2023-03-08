#!/usr/bin/env python3
""" exercise module """

import redis
import uuid
from typing import Union, Callable


class Cache:
    """ Cache class """

    def __init__(self) -> None:
        """ Instance method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store method """
        randomKey = str(uuid.uuid4())
        self._redis.set(randomKey, data)
        return randomKey

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes,
                                                          int,
                                                          float]:
        """ recovering original type """
        data = self._redis.get(key)
        if fn:
            fn(data)
        return data

    def get_str(self):
        """ Parametrize Cache.get with the correct conversion function
        """

    def get_int(self):
        """ Parametrize Cache.get with the correct conversion function
        """
