#!/usr/bin/env python3
"""3-lru_cache module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching.
    It implements the LRU caching algorithm.
    """

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data
        and manage the cache size using LRU policy.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_order.remove(key)
            self.cache_data[key] = item
            self.access_order.append(key)

            if len(self.cache_data) > self.MAX_ITEMS:
                oldest = self.access_order.pop(0)
                del self.cache_data[oldest]
                print(f"DISCARD: {oldest}")

    def get(self, key):
        """
        Return the value linked to key in self.cache_data.
        Update the access order to reflect recent use.
        """
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
