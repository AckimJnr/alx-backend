#!/usr/bin/env python3
"""FIFOCache Module"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """
    Implements FIFO Cache
    """
    def __init__(self):
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                key_removed = self.queue.popleft()
                del self.cache_data[key_removed]
                print("Discard: {}".format(key_removed))
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """Get an item from the cache"""
        if key is not None:
            try:
                return self.cache_data.get(key)
            except KeyError:
                return None