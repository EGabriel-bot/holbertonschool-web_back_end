#!/usr/bin/env python3
""" Task 0 """

import redis
import uuid
from typing import Union


class Cache:
    """ Cache class """

    def __init__(self):
        """ Instance method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store method """
        randomKey = str(uuid.uuid4())
        self._redis.set(randomKey, data)
        return randomKey
