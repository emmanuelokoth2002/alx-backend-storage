#!/usr/bin/env python3
"""
Cache module
"""
import redis
import uuid
from typing import Callable, Union
import functools

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.

    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: The decorated method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.

    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: The decorated method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        input_data = str(args)
        self._redis.rpush(input_key, input_data)

        result = method(self, *args, **kwargs)

        self._redis.rpush(output_key, result)

        return result

    return wrapper

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

    @count_calls
    @call_history
    def store(self, data: Union[bytes, str]) -> str:
        """
        Store the input data in Redis and return the generated key

        Args:
            data (bytes or str): Data to be stored

        Returns:
            str: Generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
