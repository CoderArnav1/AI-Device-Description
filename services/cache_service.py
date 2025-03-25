import json
import os
import hashlib
import logging
from config.settings import CACHE_FILE
def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            logging.warning("Cache file corrupted. Resetting cache.")
            return {}
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=4)

def get_cache_key(model_name, camera, processor, battery, display):
    input_string = f"{model_name}-{camera}-{processor}-{battery}-{display}"
    return hashlib.md5(input_string.encode()).hexdigest()

def get_cached_response(cache_key):
    cache = load_cache()
    return cache.get(cache_key)

# Save response to cache
def save_to_cache(cache_key, response):
    cache = load_cache()
    cache[cache_key] = response
    save_cache(cache)
