import pytest
from core.api_client import APIClient
from data.test_data import TestData
from config.endpoints import Endpoints  # Add this import

class TestOrdersWorkflow:
    def setup_method(self):
        self.client = APIClient()
        self.created_ids = {"products": [], "users": [], "carts": [], "orders": []}
        
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
        
        # Create test cart
        cart_data = {
            "userId": self.user_id,
            "products": [{
                "productId": self.product_id,
                "quantity": 1,
                "price": 999
            }],
            "totalAmount": 999,
            "status": "active"
        }
        cart_resp = self.client.create_cart(cart_data)
        self.cart_id = cart_resp.json()["id"]
        self.created_ids["carts"].append(self.cart_id)
    
    def teardown_method(self):
        # Cleanup in reverse order
        for order_id in self.created_ids["orders"]:
            self.client.delete(Endpoints.ORDERS, order_id)  # FIXED: Use Endpoints.ORDERS
        for cart_id in self.created_ids["carts"]:
            self.client.delete(Endpoints.CARTS, cart_id)    # FIXED: Use Endpoints.CARTS
        for product_id in self.created_ids["products"]:
            self.client.delete_product(product_id)
        for user_id in self.created_ids["users"]:
            self.client.delete(Endpoints.USERS, user_id)    # FIXED: Use Endpoints.USERS
    
    def test_create_order(self):
        """Test creating an order from cart"""
        order_data = {
            "userId": self.user_id,
            "cartId": self.cart_id,
            "items": [{
                "productId": self.product_id,
                "quantity": 1,
                "priceAtPurchase": 999
            }],
            "total": 999,
            "status": "pending",
            "shippingAddress": "123 Test Street",
            "paymentMethod": "credit_card"
        }
        
        response = self.client.create_order(order_data)
        assert response.status_code == 201
        
        order = response.json()
        assert order["userId"] == self.user_id
        assert order["cartId"] == self.cart_id
        assert order["status"] == "pending"
        
        self.created_ids["orders"].append(order["id"])
    
    def test_order_status_flow(self):
        """Test updating order status through workflow"""
        # First create order
        order_data = {
            "userId": self.user_id,
            "cartId": self.cart_id,
            "items": [{
                "productId": self.product_id,
                "quantity": 1,
                "priceAtPurchase": 999
            }],
            "total": 999,
            "status": "pending",
            "shippingAddress": "123 Test Street",
            "paymentMethod": "credit_card"
        }
        create_resp = self.client.create_order(order_data)
        order_id = create_resp.json()["id"]
        self.created_ids["orders"].append(order_id)
        
        # Update status to paid
        response = self.client.update_order_status(order_id, "paid")
        assert response.status_code == 200
        assert response.json()["status"] == "paid"
        
        # Update status to shipped
        response = self.client.update_order_status(order_id, "shipped")
        assert response.status_code == 200
        assert response.json()["status"] == "shipped"
        
        # Update status to delivered
        response = self.client.update_order_status(order_id, "delivered")
        assert response.status_code == 200
        assert response.json()["status"] == "delivered"
    
    def test_get_user_orders(self):
        """Test retrieving orders for a specific user"""
        # First create an order
        order_data = {
            "userId": self.user_id,
            "cartId": self.cart_id,
            "items": [{
                "productId": self.product_id,
                "quantity": 1,
                "priceAtPurchase": 999
            }],
            "total": 999,
            "status": "pending",
            "shippingAddress": "123 Test Street",
            "paymentMethod": "credit_card"
        }
        create_resp = self.client.create_order(order_data)
        order_id = create_resp.json()["id"]
        self.created_ids["orders"].append(order_id)
        
        # Get user's orders
        response = self.client.get_user_orders(self.user_id)
        assert response.status_code == 200
        
        user_orders = response.json()
        assert isinstance(user_orders, list)
        assert any(order["userId"] == self.user_id for order in user_orders)
