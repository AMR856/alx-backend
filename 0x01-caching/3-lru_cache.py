#!/usr/bin/python3
"""FifoCaching is created here as you can"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """This class is doing a lot of things"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", first_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Getter here"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=True)
        return self.cache_data[key]
