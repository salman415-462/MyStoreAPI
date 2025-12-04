import pytest
from core.api_client import APIClient
from data.test_data import TestData

class TestProductsCRUD:
    def setup_method(self):
        self.client = APIClient()
        self.test_product = TestData.generate_product()
        self.created_ids = []
    
    def teardown_method(self):
        for product_id in self.created_ids:
            self.client.delete_product(product_id)
    
    def test_create_product(self):
        response = self.client.create_product(self.test_product)
        assert response.status_code == 201
        product_data = response.json()
        assert "id" in product_data
        self.created_ids.append(product_data["id"])
    
    def test_read_product(self):
        create_resp = self.client.create_product(self.test_product)
        product_id = create_resp.json()["id"]
        self.created_ids.append(product_id)
        
        response = self.client.get_product(product_id)
        assert response.status_code == 200
        assert response.json()["id"] == product_id
    
    def test_get_all_products(self):
        response = self.client.get_all_products()
        assert response.status_code == 200
        assert isinstance(response.json(), list)
