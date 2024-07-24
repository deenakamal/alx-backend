#!/usr/bin/env python3
"""Defines LIFOCache class"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implement a LIFO (Last In, First Out) cache system"""

    def __init__(self):
        """Initialize the cache with an empty order list"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache with LIFO eviction policy

        If the cache exceeds its maximum size, the last item added
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
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            The value of the item if the key exists, otherwise None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
