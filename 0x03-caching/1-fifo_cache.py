#!/usr/bin/env python3
""" Task 1 """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache System """

    def __init__(self) -> None:
        """ Constructor and init super """
        super().__init__()

    def put(self, key, item) -> None:
        """ Must assign to cache_data the item value for key"""
        if key and item:
            if (len(self.cache_data.keys()) == self.MAX_ITEMS):
                k = list(self.cache_data.keys())[0]
                del self.cache_data[k]
                print("DISCARD: {}".format(k))
            self.cache_data.update({key: item})

    def get(self, key):
        """ Must return the value in self.cache_data linked to key """
        if key:
            try:
                return self.cache_data.get(key)
            except KeyError:
                return None
        return None
