#!/usr/bin/python3
"""class LIFOCache that inherits from BaseCaching."""


from typing import Union
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Fifo class
    Args:
        BaseCaching (class): base cache class
    """

    def __init__(self):
        super().__init__()

    def put(self, key: str, item: str) -> None:
        """Add value en cache."""
        if key and item:
            new_dict = {key: item}
            self.isFillCache()
            self.cache_data = new_dict

    def get(self, key: str) -> Union[None, object]:
        """Get value of cache"""
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

    def isFillCache(self) -> None:
        """check if cache not is fill"""
        if len(self.cache_data.keys()) >= self.MAX_ITEMS:
            first_element = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_element)
            print(f'DISCARD: {first_element}')
            return True
        return False
