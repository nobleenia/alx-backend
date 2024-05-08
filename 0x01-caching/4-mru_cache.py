#!/usr/bin/env python3
"""4-mru_cache module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and is a caching system
    that discards the most recently used item (MRU algorithm).
    """

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data.
        Discard the most recently used item if the cache exceeds MAX_ITEMS.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_order.remove(key)
            self.cache_data[key] = item
            self.access_order.append(key)

            if len(self.cache_data) > self.MAX_ITEMS:
                mru_key = self.access_order.pop(-1)  # Get the most recently used
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

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
