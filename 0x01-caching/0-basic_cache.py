#!/usr/bin/env python3
"""0-basic_cache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and is a
    caching system without a limit.
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key
        If key or item is None, do not do anything
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to key in self.cache_data
        Return None if key is None or
        key does not exist in self.cache_data
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
