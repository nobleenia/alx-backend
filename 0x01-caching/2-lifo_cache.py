#!/usr/bin/env python3
"""2-lifo_cache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and is a caching system
    that discards the last item put in the cache (LIFO).
    """

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data.
        Discard the last item if the cache exceeds the max size.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                if self.last_key:
                    discarded = self.last_key
                    del self.cache_data[discarded]
                    print("DISCARD: {}".format(discarded))
            self.last_key = key

    def get(self, key):
        """
        Return the value linked to key in self.cache_data.
        Return None if key is None or if the key doesn’t exist.
        """
        return self.cache_data.get(key, None)
