import requests
from config.endpoints import Endpoints

class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
    
    # Generic CRUD methods
    def create(self, endpoint, data):
        return self.session.post(endpoint, json=data)
    
    def read(self, endpoint, item_id=None):
        url = f"{endpoint}/{item_id}" if item_id else endpoint
        return self.session.get(url)
    
    def update(self, endpoint, item_id, data):
        url = f"{endpoint}/{item_id}"
        return self.session.put(url, json=data)
    
    def delete(self, endpoint, item_id):
        url = f"{endpoint}/{item_id}"
        return self.session.delete(url)
    
    # Product-specific methods
    def create_product(self, product_data):
        return self.create(Endpoints.PRODUCTS, product_data)
    
    def get_all_products(self):
        return self.read(Endpoints.PRODUCTS)
    
    def get_product(self, product_id):
        return self.read(Endpoints.PRODUCTS, product_id)
    
    def update_product(self, product_id, update_data):
        return self.update(Endpoints.PRODUCTS, product_id, update_data)
    
    def delete_product(self, product_id):
        return self.delete(Endpoints.PRODUCTS, product_id)
    
    def get_products_by_category(self, category):
        url = Endpoints.PRODUCTS_BY_CATEGORY.format(category=category)
        return self.session.get(url)
    
    # User methods
    def create_user(self, user_data):
        return self.create(Endpoints.USERS, user_data)
    
    def get_user(self, user_id):
        return self.read(Endpoints.USERS, user_id)
    
    # Cart methods
    def create_cart(self, cart_data):
        return self.create(Endpoints.CARTS, cart_data)
    
    def get_user_carts(self, user_id):
        url = Endpoints.USER_CARTS.format(userId=user_id)
        return self.session.get(url)
    
    # Order methods
    def create_order(self, order_data):
        return self.create(Endpoints.ORDERS, order_data)
    
    def get_user_orders(self, user_id):
        url = Endpoints.USER_ORDERS.format(userId=user_id)
        return self.session.get(url)
    
    def update_order_status(self, order_id, new_status):
        return self.update(Endpoints.ORDERS, order_id, {"status": new_status})
