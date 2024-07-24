#!/usr/bin/env python3
"""Defines BasicCache class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Creats a class BasicCashe inherts from BaseCaching class"""
    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Assign a new key/value to the dictionary"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves value of a specific key from the dict"""
        if key is None or not self.cache_data.get(key):
            return None

        return self.cache_data.get(key)
