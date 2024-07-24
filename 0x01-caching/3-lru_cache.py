#!/usr/bin/env python3
"""Defines LRUCache class"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implement an LRU (Least Recently Used) cache system"""

    def __init__(self):
        """Initialize the LRUCache with an empty access order list"""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """Add an item to the cache with LRU eviction policy

        If the cache exceeds its maximum size, the least recently used item
        will be discarded.

        Args:
            key (str): The key for the item.
            item (any): The value of the item.

        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """Retrieve an item from the cache

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            The value of the item if the key exists, otherwise None.
        """
        value = self.cache_data.get(key)

        if value is not None:
            self.access_order.remove(key)
            self.access_order.append(key)

        return value
