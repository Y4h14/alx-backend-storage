#!/usr/bin/env python3
"""defines a Cache class"""
import redis
import uuid
from typing import Any, Callable, Union


class Cache:
    """
    A class for creating a cahce
    """
    def __init__(self) -> None:
        """
        initalize the redis cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        creates a key for the data, and store the data on redis
        Parameters:
        data (Any): the data to be stored

        Returns:
        (string) : the key where the passed data is stored
        """
        key_id = str(uuid.uuid4())
        self._redis.set(key_id, data)
        return key_id
    

    def get(self, key: str, fn: Callable) -> Union[str, int, float, bytes]:
        """
        takes a key string and a callable to convert redis data
        Parameters:
            key (str): the key for the data
            fn (Callable) : function that can be used to convert data
                            back to the desired format
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data


    def get_str(self, key: str) -> str:
        """
            conversts string format
        """
        return self.get(key, lambda x: x.decode('utf-8'))


    def get_int(self, key: str) -> int:
        """
        converts a byte string into an int
        """
        return self.get(key, lambda x: int(x))
