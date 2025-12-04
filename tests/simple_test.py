import pytest
from core.api_client import APIClient

def test_simple_api():
    """Simple test without teardown issues"""
    client = APIClient()
    
    # Test 1: Get products
    response = client.get_all_products()
    print(f"GET /products: {response.status_code}")
    assert response.status_code == 200
    
    # Test 2: Create a product
    product = {
        "name": "Test Product",
        "price": 99.99,
        "category": "test"
    }
    response = client.create_product(product)
    print(f"POST /products: {response.status_code}")
    assert response.status_code == 201
    
    print("✅ All simple tests passed!")
