#!/usr/bin/python3
"""BasicCache is created here as you can"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """You don't like the class name?"""
    def put(self, key, item):
        """I'm putting in here"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Getter here"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
