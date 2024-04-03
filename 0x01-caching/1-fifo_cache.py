#!/usr/bin/env python3
"""FIFOCache Module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching class"""

    def __init__(self):
        """Constructor"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                first_item = next(iter(self.cache_data))
                del self.cache_data[first_item]
                print("DISCARD:", first_item)

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from cache"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]