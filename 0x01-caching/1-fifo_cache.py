#!/usr/bin/python3
"""FifoCaching is created here as you can"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """The class is named after a queue as you can see,
    I could use a queue data structure instead of a list
    ain't gonna lie"""
    def __init__(self):
        super().__init__()
        self.order_list = []

    def put(self, key, item):
        """Putter fucntion"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            self.order_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                the_key_to_remove = self.order_list[0]
                self.order_list = self.order_list[1:]
                self.cache_data.pop(the_key_to_remove)
                print(f'DISCARD: {the_key_to_remove}')

    def get(self, key):
        """Getter here"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
