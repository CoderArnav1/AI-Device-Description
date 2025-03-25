import os
import logging
import time
from dotenv import load_dotenv

load_dotenv()


LOG_DIR = "logs"
CACHE_DIR = "cache"
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

LOG_FILE = os.getenv("LOG_FILE", os.path.join(LOG_DIR, "app.log"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    filename=LOG_FILE,
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
)

logger = logging.getLogger(__name__)
logger.info("Logging is correctly set up!")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

CACHE_FILE = os.getenv("CACHE_FILE", os.path.join(CACHE_DIR, "device_cache.json"))
logger.info(f"Cache File Location: {CACHE_FILE}")

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
logger.info(f"Server running on {HOST}:{PORT}")

