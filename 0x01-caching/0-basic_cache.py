#!/usr/bin/env python3
""" Basic Caching Module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        BasicCache is a caching system and inherits from BaseCaching
    """

    def put(self, key, item):
        """ Assigns a kv pair to the cache_data dict """

        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ gets an item from the cache_data dict by its key """

        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
