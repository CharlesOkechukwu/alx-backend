#!/usr/bin/env python3
"""module for class to implement a LIFO caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """a basic cache class the implements the LIFO caching Technique"""
    def __init__(self):
        """initialize class instance attributes"""
        super().__init__()
        self._queue = []

    def put(self, key, item):
        """add or remove key/value pair"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self._queue:
                self._queue.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                out_key = self._queue.pop(-2)
                del self.cache_data[out_key]
                print("DISCARD: {}".format(out_key))

    def get(self, key):
        """return value for key in self.cache_data or None"""
        if key is not None:
            return self.cache_data.get(key, None)
        return None
