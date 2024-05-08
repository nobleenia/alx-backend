#!/usr/bin/env python3
"""100-lfu_cache module"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching, is a caching
    system that discards the least frequently used items.
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage_frequency = {}
        self.items = OrderedDict()

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data.
        Discard least frequent item or the LRU if there is a tie.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS and \
               key not in self.cache_data:
                self.evict()
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            # Move the key to the end to maintain LRU order
            if key in self.items:
                self.items.move_to_end(key)
            else:
                self.items[key] = None

    def get(self, key):
        """
        Return the value linked to key in self.cache_data.
        Increase frequency, update the timestamp,
        and return the value.
        """
        if key in self.cache_data:
            self.usage_frequency[key] += 1
            self.items.move_to_end(key)
            return self.cache_data[key]
        return None

    def evict(self):
        """
        Evict items based on LFU policy, and in case of a tie,
        based on LRU policy.
        """
        if not self.items:
            return
        # Find the least frequently used item
        least_freq = min(self.usage_frequency.values())
        # Collect all candidates with the same least frequency
        least_freq_keys = [
            k for k, v in self.usage_frequency.items() if v == least_freq
        ]
        # Use the first inserted item for tie-breaking
        for key in self.items:
            if key in least_freq_keys:
                self.cache_data.pop(key, None)
                self.usage_frequency.pop(key, None)
                self.items.pop(key, None)
                print(f"DISCARD: {key}")
                break
