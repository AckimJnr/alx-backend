#!/usr/bin/env python3
"""FIFO Cache Module

This module implements a FIFO (First In, First Out) caching mechanism.
It provides the FIFOCache class, which inherits from BaseCaching, to
implement a caching system based on the FIFO algorithm. In this algorithm,
the first item inserted is the first to be removed when the cache reaches
its maximum capacity.

Classes:
    FIFOCache: Implements a FIFO caching mechanism.

"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Implements a FIFO (First In, First Out) caching mechanism.

    This class inherits from BaseCaching and provides a caching system
    based on the FIFO algorithm, where the first item inserted is the
    first to be removed when the cache reaches its maximum capacity.

    Attributes:
        MAX_ITEMS (int): Maximum number of items the cache can hold.

    Methods:
        __init__(): Initializes the FIFOCache instance.
        put(key, item): Adds an item to the cache.
        get(key): Retrieves an item from the cache.
    """

    def __init__(self):
        """
        Construct and overload super constructor
        Return:
            None
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        Args:
            key: key to be created
            item: item for the dictionary
        Return:
            None if key or item is None
            Else add item to dict
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                first_item = next(iter(self.cache_data))
                del self.cache_data[first_item]
                print("DISCARD:", first_item)

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from cache
        Args:
            key: key to retrieve item from the cache
        Return:LIFOCache
            None if key is none or key is not available
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
