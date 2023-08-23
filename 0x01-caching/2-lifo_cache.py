#!/usr/bin/env python3
""" LIFO Caching Module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        LIFOCache is a caching system and inherits from BaseCaching
    """

    def __init__(self):
        """
            Initialization instance init
        """

        super().__init__()

    def put(self, key, item):
        """
            Insert a new item in the cache data, behaving like a stack
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(last_item))
            self.cache_data.pop(last_item)

    def get(self, key):
        """
            Retrieves an item from cache data by key
        """

        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
