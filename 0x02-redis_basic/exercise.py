#!/usr/bin/env python3
"""
Cache module
"""
import redis
import uuid
from typing import Callable, Union

class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Initialize a Redis cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        """
        Store the input data in Redis and return the generated key

        Args:
            data (bytes): Data to be stored

        Returns:
            str: Generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[bytes], Union[str, int, bytes]] = None) -> Union[str, int, bytes, None]:
        """
        Retrieve data from Redis for the given key and optionally convert it using a callable function.

        Args:
            key (str): Key to retrieve from Redis.
            fn (Callable, optional): Callable function to convert the data. Defaults to None.

        Returns:
            Union[str, int, bytes, None]: Retrieved data, possibly converted using the provided callable.
        """
        data = self._redis.get(key)
        if data and fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve a string from Redis for the given key.

        Args:
            key (str): Key to retrieve from Redis.

        Returns:
            Union[str, None]: Retrieved string or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve an integer from Redis for the given key.

        Args:
            key (str): Key to retrieve from Redis.

        Returns:
            Union[int, None]: Retrieved integer or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: int(d))
