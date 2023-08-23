#!/usr/bin/env python3
""" This module contains the class LFUCache """
from base_caching import BaseCaching
from datetime import datetime


def all_least_freq(cache_frequency, least_frequent):
    """ Retrieves all keys with smallest frequency """

    least_frequent_keys = []
    for key, value in cache_frequency.items():
        if value == least_frequent:
            least_frequent_keys.append(key)
    return least_frequent_keys


class LFUCache(BaseCaching):
    """ This class implements a LFU caching system """

    def __init__(self):
        """ Initialize the class instance """

        super().__init__()
        self.cache_queue = {}
        self.cache_frequency = {}

    def put(self, key, item):
        """ Adds a kv pair to the cache dictionary """

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                least_frequent = min(self.cache_frequency.values())
                least_frequent_keys = all_least_freq(
                    self.cache_frequency,
                    least_frequent)
                if len(least_frequent_keys) == 1:
                    discard = least_frequent_keys[0]
                else:
                    all_least_frequent = {
                        key: self.cache_queue[key]
                        for key in least_frequent_keys
                        }
                    discard = min(
                        all_least_frequent,
                        key=all_least_frequent.get)
                del self.cache_data[discard]
                del self.cache_queue[discard]
                del self.cache_frequency[discard]
                print("DISCARD: {}".format(discard))

            self.cache_frequency[key] = self.cache_frequency.get(key, 0) + 1
            self.cache_queue[key] = datetime.now()

    def get(self, key):
        """ Retrieves the item associated with key """

        if key and key in self.cache_data:
            self.cache_frequency[key] += 1
            self.cache_queue[key] = datetime.now()
            return self.cache_data.get(key)
