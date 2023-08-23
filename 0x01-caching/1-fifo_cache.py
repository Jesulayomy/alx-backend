#!/usr/bin/env python3
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ The First in first out caching system """

    def __init__(self):
        """
            Initialization instance method
        """
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """ Insert a new item in the cache data, behaving like a list """

        if key and item:
            self.cache_data[key] = item
            self.cache_list.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = self.cache_list.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Retrieves an item from cache data by key """

        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data.get(key)
