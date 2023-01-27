#!/usr/bin/env python3
""" Task 0 """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Caching System """
    def __init__(self) -> None:
        """ Constructor and init super """
        super().__init__()

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data
            the item value for the key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key:
            try:
                return self.cache_data.get(key)
            except KeyError:
                return None
        return None
