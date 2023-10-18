#!/usr/bin/env python3
"""
Cache module
"""
import redis
import uuid

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
