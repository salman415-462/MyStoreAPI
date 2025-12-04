import pytest
from core.api_client import APIClient
from data.test_data import TestData
from config.endpoints import Endpoints  # Add this import

class TestUsersCRUD:
    def setup_method(self):
        self.client = APIClient()
        self.test_user = TestData.generate_user()
        self.created_user_ids = []
    
    def teardown_method(self):
        for user_id in self.created_user_ids:
            self.client.delete(Endpoints.USERS, user_id)  # FIXED: Use Endpoints.USERS
    
    def test_create_user(self):
        """Test creating a new user"""
        response = self.client.create_user(self.test_user)
        
        assert response.status_code == 201
        user_data = response.json()
        
        assert "id" in user_data
        assert user_data["username"] == self.test_user["username"]
        assert user_data["email"] == self.test_user["email"]
        
        self.created_user_ids.append(user_data["id"])
    
    def test_get_user(self):
        """Test retrieving a user"""
        # Create user first
        create_resp = self.client.create_user(self.test_user)
        user_id = create_resp.json()["id"]
        self.created_user_ids.append(user_id)
        
        # Get user
        response = self.client.get_user(user_id)
        
        assert response.status_code == 200
        assert response.json()["id"] == user_id
