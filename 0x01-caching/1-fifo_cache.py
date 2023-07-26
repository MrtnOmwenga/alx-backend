#!/usr/bin/env python3
"""
FIFO Caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching class """

    def __init__(self):
        """ Initialize class """
        super().__init__()

    def put(self, key, item):
        """ Add data to cache """
        if key is None or item is None:
            return

        cache = self.cache_data
        if key not in cache and len(cache) == self.MAX_ITEMS:
            first = list(self.cache_data)[0]
            del self.cache_data[first]
            print('DISCARD: {}'.format(first))

        self.cache_data[key] = item

    def get(self, key):
        """ Get data from cache """
        if key is None:
            return None

        try:
            return self.cache_data[key]
        except KeyError:
            return None
