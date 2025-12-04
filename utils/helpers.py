import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_response(response):
    """Log API response details"""
    logger.info(f"URL: {response.url}")
    logger.info(f"Status: {response.status_code}")
    logger.info(f"Response Time: {response.elapsed.total_seconds():.2f}s")
    return response

def validate_response(response, expected_status=200):
    """Validate response status code"""
    if response.status_code != expected_status:
        logger.error(f"Expected {expected_status}, got {response.status_code}")
        logger.error(f"Response: {response.text}")
        return False
    return True

def print_json(data):
    """Pretty print JSON data"""
    print(json.dumps(data, indent=2))
