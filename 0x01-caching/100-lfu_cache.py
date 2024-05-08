#!/usr/bin/env python3
"""100-lfu_cache module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and is a caching system
    that discards the least frequently used items.
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage_frequency = {}
        self.time_stamp = {}

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data.
        Discard the least frequency used item or the LRU if there is a tie.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.usage_frequency:
                self.usage_frequency[key] += 1
            else:
                self.usage_frequency[key] = 1
            self.time_stamp[key] = self.current_time_stamp()

            if len(self.cache_data) > self.MAX_ITEMS:
                least_freq = min(self.usage_frequency.values())
                least_freq_keys = [k for k, v in self.usage_frequency.items() if v == least_freq]
                if len(least_freq_keys) == 1:
                    lfu_key = least_freq_keys[0]
                else:
                    # Tie situation: use LRU
                    lfu_key = sorted(least_freq_keys, key=lambda k: self.time_stamp[k])[0]

                self.cache_data.pop(lfu_key)
                self.usage_frequency.pop(lfu_key)
                self.time_stamp.pop(lfu_key)
                print(f"DISCARD: {lfu_key}")

    def get(self, key):
        """
        Return the value linked to key in self.cache_data.
        Increase frequency, update the timestamp, and return the value.
        """
        if key in self.cache_data:
            self.usage_frequency[key] += 1
            self.time_stamp[key] = self.current_time_stamp()
            return self.cache_data[key]
        return None

    def current_time_stamp(self):
        """Return a monotonically increasing time stamp."""
        from time import monotonic
        return monotonic()
