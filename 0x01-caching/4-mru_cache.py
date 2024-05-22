#!/usr/bin/env python3
"""module to implement basic caching class that uses MRU caching
technique"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """a basic cache class which uses the MRU caching technique"""
    def __init__(self):
        """initialize class instance attributes"""
        super().__init__()
        self._queue = []

    def put(self, key, item):
        """add or remove key/value pair from cache using MRU algorithm"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self._queue:
                self._queue.remove(key)
            self._queue.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                out_key = self._queue.pop(-2)
                del self.cache_data[out_key]
                print("DISCARD: {}".format(out_key))

    def get(self, key):
        """return value for key in self.cache_data or None"""
        if key is not None:
            if key in self._queue:
                self._queue.remove(key)
                self._queue.append(key)
        return self.cache_data.get(key, None)
