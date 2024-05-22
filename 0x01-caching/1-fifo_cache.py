#!/usr/bin/env python3
"""module for class for FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """a basic cache class that uses the FIFO caching technique"""
    def __init__(self):
        """intialize class instance attributes"""
        super().__init__()
        self._queue = []

    def put(self, key, item):
        """add or remove key/value pair from cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self._queue:
                self._queue.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                out_key = self._queue.pop(0)
                del self.cache_data[out_key]
                print("DISCARD: {}".format(out_key))

    def get(self, key):
        """return value for key in self.cache_data or None"""
        if key is not None:
            return self.cache_data.get(key, None)
        return None
