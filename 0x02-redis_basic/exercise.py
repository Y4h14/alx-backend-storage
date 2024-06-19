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

