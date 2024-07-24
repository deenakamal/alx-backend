#!/usr/bin/env python3
"""Defines MRUCache class"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """Implement a Most Recently Used (MRU) cache system"""

    def __init__(self):
        """Initialize the MRUCache with an empty attribute for tracking the most recently used item"""
        super().__init__()
        self.most_recent_key = None

    def put(self, key, item):
        """Add an item to the cache with MRU eviction policy

        If the cache exceeds its maximum size, the most recently used item
        will be discarded.

        Args:
            key (str): The key for the item.
            item (any): The value of the item.

        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if self.most_recent_key is not None:
                del self.cache_data[self.most_recent_key]
                print(f"DISCARD: {self.most_recent_key}")

        self.cache_data[key] = item
        self.most_recent_key = key

    def get(self, key):
        """Retrieve an item from the cache

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            The value of the item if the key exists, otherwise None.
        """
        value = self.cache_data.get(key)

        if value is not None:
            self.most_recent_key = key

        return value
