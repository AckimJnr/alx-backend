#!/usr/bin/env python3
"""BasicCacheModule
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Implement basic cache"""

    def put(self, key, value):
        """
        Adds an item to the cache
        """
        if key is None or value is None:
            pass
        else:
            self.cache_data[key] = value

    def get(self, key):
        """
        get item from cache
        """
        if key is not None:
            try:
                return self.cache_data.get(key)
            except KeyError:
                return None
