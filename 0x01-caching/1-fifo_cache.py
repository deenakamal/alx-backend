#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """ FIFOCache class inherits from BaseCaching
    Implements a FIFO (First In, First Out) caching system.
    """

    def __init__(self):
        """ Initialize the FIFOCache instance
        Sets up the cache_data dictionary and an order deque
        to keep track of the order in which items are added.
        """
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """ Add an item to the cache
        Args:
            key (str): The key to associate with the item.
            item (any): The value to store in the cache.
        
        If the key or item is None, do nothing.
        If the cache exceeds the maximum allowed items, 
        evicts the oldest item (FIFO) and prints a discard message.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                oldest_key = self.order.popleft()
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache
        Args:
            key (str): The key for the item to retrieve.
        
        Returns:
            The value associated with the key if it exists, 
            otherwise returns None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
