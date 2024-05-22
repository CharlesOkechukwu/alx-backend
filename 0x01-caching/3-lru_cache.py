#!/usr/env python3
"""module for class cache replacement with LRU algorithm"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """basic cache class that uses the LRU caching technique"""
    def __init__(self):
        """initialize class instance attributes"""
        super().__init__()
        self._queue = []
    
    def put(self, key, item):
        """add or remove key/value pair using LRU algorithm"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self._queue:
                self._queue.remove(key)
            self._queue.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                out_key = self._queue.pop(0)
                del self.cache_data[out_key]
                print("DISCARD: {}".format(out_key))
    
    def get(self, key):
        """return value for key in self.cache_data or None"""
        if key is not None:
            if key in self._queue:
                self._queue.remove(key)
                self._queue.append(key)
        return self.cache_data.get(key, None)