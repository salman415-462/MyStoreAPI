import pytest
from core.api_client import APIClient
from data.test_data import TestData
from config.endpoints import Endpoints  # Add this import

class TestCartWorkflows:
    def setup_method(self):
        self.client = APIClient()
        self.created_ids = {"products": [], "users": [], "carts": []}
        
        # Create test user
        user = TestData.generate_user()
        user_resp = self.client.create_user(user)
        self.user_id = user_resp.json()["id"]
        self.created_ids["users"].append(self.user_id)
        
        # Create test product
        product = TestData.generate_product()
        product_resp = self.client.create_product(product)
        self.product_id = product_resp.json()["id"]
        self.created_ids["products"].append(self.product_id)
    
    def teardown_method(self):
        # Cleanup in reverse order
        for cart_id in self.created_ids["carts"]:
            self.client.delete(Endpoints.CARTS, cart_id)  # FIXED: Use Endpoints.CARTS
        for product_id in self.created_ids["products"]:
            self.client.delete_product(product_id)
        for user_id in self.created_ids["users"]:
            self.client.delete(Endpoints.USERS, user_id)  # FIXED: Use Endpoints.USERS
    
    def test_create_cart_with_products(self):
        """Test creating a shopping cart with products"""
        cart_data = {
            "userId": self.user_id,
            "products": [{
                "productId": self.product_id,
                "quantity": 2,
                "price": 999
            }],
            "totalAmount": 1998,
            "status": "active"
        }
        
        response = self.client.create_cart(cart_data)
        assert response.status_code == 201
        
        cart = response.json()
        assert cart["userId"] == self.user_id
        assert len(cart["products"]) == 1
        assert cart["products"][0]["productId"] == self.product_id
        
        self.created_ids["carts"].append(cart["id"])
    
    def test_get_user_carts(self):
        """Test retrieving carts for a specific user"""
        # Create a cart first
        cart_data = {
            "userId": self.user_id,
            "products": [],
            "totalAmount": 0,
            "status": "active"
        }
        create_resp = self.client.create_cart(cart_data)
        cart_id = create_resp.json()["id"]
        self.created_ids["carts"].append(cart_id)
        
        # Get user's carts
        response = self.client.get_user_carts(self.user_id)
        assert response.status_code == 200
        
        user_carts = response.json()
        assert isinstance(user_carts, list)
        assert any(cart["userId"] == self.user_id for cart in user_carts)
