import requests
import redis
from typing import Callable

def cache_url_access_count(fn: Callable) -> Callable:
    """
    Decorator to cache URL access count with a 10-second expiration.
    """
    def wrapper(url: str) -> str:
        redis_client = redis.Redis()
        key = f"count:{url}"

        # Check if URL count is cached
        count = redis_client.get(key)
        if count:
            count = int(count)
            redis_client.setex(key, 10, count + 1)
        else:
            count = 1
            redis_client.setex(key, 10, count)

        return fn(url)

    return wrapper

@cache_url_access_count
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
