#!/usr/bin/env python3
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ The First in first out caching system """

    def __init__(self):
        """
            Initialization instance method
        """
        super().__init__()

    def put(self, key, item):
        """ Insert a new item in the cache data, behaving like a queue """

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_item = list(self.cache_data.keys())[0]
            print("DISCARD: {}".format(first_item))
            self.cache_data.pop(first_item)

    def get(self, key):
        """ Retrieves an item from cache data by key """

        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data.get(key)
