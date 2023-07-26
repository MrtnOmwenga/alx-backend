#!/usr/bin/env python3
"""
MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU caching class """

    def __init__(self):
        """ Initialize class """
        super().__init__()
        self.use_tracker = {}

    def log_use(self, key):
        """ Log Use of a resource in cache """
        if key is not None:
            if len(self.use_tracker) != 0:
                self.use_tracker[key] = max(self.use_tracker.values()) + 1
            else:
                self.use_tracker[key] = 0
        # print(self.use_tracker)

    def put(self, key, item):
        """ Add data to cache """
        if key is None or item is None:
            return

        cache = self.cache_data
        if key not in cache and len(cache) == self.MAX_ITEMS:
            _key = lambda x: self.use_tracker[x]
            least_used = max(self.use_tracker, key=_key)
            del self.cache_data[least_used],  self.use_tracker[least_used]
            print('DISCARD: {}'.format(least_used))

        self.cache_data[key] = item
        self.log_use(key)

    def get(self, key):
        """ Get data from cache """
        if key is None:
            return None

        try:
            result = self.cache_data[key]
            self.log_use(key)
            return result
        except KeyError:
            return None
