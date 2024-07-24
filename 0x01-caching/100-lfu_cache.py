#!/usr/bin/env python3
"""Defines LFUCache class"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Implement an LFU (Least Frequently Used) cache system"""

    def __init__(self):
        """Initialize LFUCache with an empty frequency list"""
        super().__init__()
        self.frequency_list = []

    def put(self, key, item):
        """Add an item to the cache with LFU eviction policy

        If the cache exceeds its maximum size, the least frequently used item
        will be discarded. If there are multiple items with the same frequency,
        the least recently used item among them will be discarded.

        Args:
            key (str): The key for the item.
            item (any): The value of the item.

        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.update_frequency_and_move_to_end(key)
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_freq = min(self.frequency_list, key=lambda x: x[1])
            del self.cache_data[min_freq[0]]
            self.frequency_list.remove(min_freq)
            print(f"DISCARD: {min_freq[0]}")

        self.cache_data[key] = item
        self.frequency_list.append((key, 1))

    def get(self, key):
        """Retrieve an item from the cache

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            The value of the item if the key exists, otherwise None.
        """
        value = self.cache_data.get(key)

        if value:
            self.update_frequency_and_move_to_end(key)

        return value

    def update_frequency_and_move_to_end(self, key):
        """Update frequency of the key and move,
        its corresponding tuple to the end

        Args:
            key (str): The key for which the frequency needs to be updated.
        """
        for i, (existing_key, frequency) in enumerate(self.frequency_list):
            if existing_key == key:
                self.frequency_list[i] = (key, frequency + 1)
                self.frequency_list.append(self.frequency_list.pop(i))
                break
