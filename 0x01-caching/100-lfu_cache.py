#!/usr/bin/env python3
"""100-lfu_cache module"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and is
    a caching system that discards the least frequent items
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage_frequency = {}
        self.time_stamp = {}
        self.counter = 0

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data
        Discard the least frequency used item or LRU if tied
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.usage_frequency[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    self.evict()
                self.usage_frequency[key] = 1
            self.cache_data[key] = item
            self.time_stamp[key] = self.counter
            self.counter += 1

    def get(self, key):
        """
        Return the value linked to key in self.cache_data.
        Increase frequency, update timestamp, return value
        """
        if key in self.cache_data:
            self.usage_frequency[key] += 1
            self.time_stamp[key] = self.counter
            self.counter += 1
            return self.cache_data[key]
        return None

    def evict(self):
        """Evict items based on LFU and LRU strategy."""
        if not self.cache_data:
            return
        
        least_freq = min(self.usage_frequency.values())
        lfu_candidates = [k for k, v in self.usage_frequency.items() if v == least_freq]
        lfu_key = min(lfu_candidates, key=lambda k: self.time_stamp[k])
        
        self.cache_data.pop(lfu_key)
        self.usage_frequency.pop(lfu_key)
        self.time_stamp.pop(lfu_key)
        print(f"DISCARD: {lfu_key}")
