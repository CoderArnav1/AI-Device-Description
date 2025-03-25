import ollama
import logging
from services.cache_service import get_cache_key, get_cached_response, save_to_cache
from config.settings import OLLAMA_MODEL

def generate_device_description(model_name, camera, processor, battery, display):
    cache_key = get_cache_key(model_name, camera, processor, battery, display)

    # Check cache first
    cached_response = get_cached_response(cache_key)
    if cached_response:
        logging.info(f"Using cached response for: {model_name}")
        return cached_response

    # AI prompt
    prompt = f"""
    You are a technology expert writing detailed product descriptions for new devices.
    Given the following specifications, generate a well-structured and sophisticated description.

    **Device Specifications:**
    - **Model Name**: {model_name if model_name else "Unknown"}
    - **Camera**: {camera if camera else "Not specified"}
    - **Processor**: {processor if processor else "Not mentioned"}
    - **Battery**: {battery if battery else "Unknown"}
    - **Display**: {display if display else "Not specified"}

    **Your response should include:**
    1. **Overview**
    2. **Key Features**
    3. **Performance Expectations**
    4. **Ideal Use Cases**
    """

    try:
        response = ollama.chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": prompt}])
        generated_text = response.get("message", {}).get("content", "❌ Failed to generate description.")

        save_to_cache(cache_key, generated_text)

        logging.info(f"Generated response for: {model_name}")
        return generated_text

    except Exception as e:
        logging.error(f"Error generating description: {str(e)}")
        return "❌ Error generating description."
