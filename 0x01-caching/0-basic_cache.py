#!/usr/bin/env python3
"""Class module for basic cache implementation"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """a basic cache implemetation class that inherits from
    BaseCaching"""
    def put(self, key, item):
        """add key/value pair to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return value in self.cache_data for a given key"""
        if key is not None:
            return self.cache_data.get(key)
        return None
