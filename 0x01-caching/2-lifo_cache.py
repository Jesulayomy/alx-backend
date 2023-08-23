#!/usr/bin/env python3
""" LIFO Caching Module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        LIFOCache is a caching system and inherits from BaseCaching
    """

    def __init__(self):
        """ Initialization instance init """

        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """
            Insert a new item in the cache data, behaving like a stack
        """

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = self.cache_list.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_list.append(key)

    def get(self, key):
        """
            Retrieves an item from cache data by key
        """

        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
