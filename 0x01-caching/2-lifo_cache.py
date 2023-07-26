#!/usr/bin/env python3
"""
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching class """

    def __init__(self):
        """ Initialize class """
        super().__init__()

    def put(self, key, item):
        """ Add data to cache """
        if key is None or item is None:
            return

        cache = self.cache_data
        if key not in cache and len(cache) == self.MAX_ITEMS:
            last = list(self.cache_data)[-1]
            del self.cache_data[last]
            print('DISCARD: {}'.format(last))

        self.cache_data[key] = item

    def get(self, key):
        """ Get data from cache """
        if key is None:
            return None

        try:
            return self.cache_data[key]
        except KeyError:
            return None
