#!/usr/bin/env python3
""" Task 0 """

import redis
import uuid
import datetime


class Cache:
    """ Cache class """

    def __init__(self):
        """ Instance method """
        self.__redis = redis.Redis()
        self.__redis.flushdb()
        print(type(self))

    def store(self, data: str) -> str:
        """ Store method """
        randomKey = str(uuid.uuid4())
        key = self.__redis.set(randomKey, data)
        return randomKey
