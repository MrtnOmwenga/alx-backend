#!/uar/bin/env python3
"""
Basic dictionary caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic dictionary cache """
    def __init__(self, **kwargs):
        """ Initialise class """
        super().__init__()

    def put(self, key, item):
        """ Add data to cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get data from cache """
        if key is None:
            return None

        try:
            return self.cache_data[key]
        except KeyError:
            return None
