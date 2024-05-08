#!/usr/bin/env python3
"""1-fifo_cache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and is a caching system.
    It implements the FIFO caching algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data.
        If the cache exceeds its max size, remove the oldest item.
        """
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the first item put in cache (FIFO)
                oldest_key = self.key_order.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD: {}".format(oldest_key))
            
            self.cache_data[key] = item
            if key in self.key_order:
                self.key_order.remove(key)
            self.key_order.append(key)

    def get(self, key):
        """
        Return the value linked to key in self.cache_data.
        Return None if key is None or does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
