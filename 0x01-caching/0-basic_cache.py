#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching system without item limit"""

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key"""
        if key is None:
            return None
        return self.cache_data.get(key)

