#!/usr/bin/env python3
""" LRU Caching Module """
from base_caching import BaseCaching
from datetime import datetime


class LRUCache(BaseCaching):
    """ Last Recently Used Caching System """

    def __init__(self):
        """ Initialization for the class """
        super().__init__()
        self.cache_queue = {}

    def put(self, key, item):
        """ Inserts a kv pair into the cache_dict and removes the LRU """

        if key and item:
            self.cache_data[key] = item
            self.cache_queue[key] = datetime.now()
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = min(self.cache_queue, key=self.cache_queue.get)
                del self.cache_data[discard]
                del self.cache_queue[discard]
                print("DISCARD: {}".format(discard))

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache data by key """

        if key and key in self.cache_data:
            self.cache_queue[key] = datetime.now()
            return self.cache_data.get(key)
