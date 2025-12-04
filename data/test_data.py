from faker import Faker

fake = Faker()

class TestData:
    @staticmethod
    def generate_product():
        return {
            "name": fake.word().capitalize() + " " + fake.word(),
            "price": round(fake.random_number(digits=3), 2),
            "category": fake.random_element(["electronics", "clothing", "books", "home"]),
            "stock": fake.random_int(min=1, max=100),
            "description": fake.sentence(),
            "imageUrl": fake.image_url(),
            "isActive": True,
            "tags": [fake.word() for _ in range(3)],
            "rating": round(fake.random.uniform(1, 5), 1)
        }
    
    @staticmethod
    def generate_user():
        return {
            "username": fake.user_name(),
            "email": fake.email(),
            "password": fake.password(),
            "role": fake.random_element(["customer", "admin"])
        }
    
    @staticmethod
    def generate_cart(user_id, products):
        return {
            "userId": user_id,
            "products": products,
            "totalAmount": sum(p["price"] * p["quantity"] for p in products),
            "status": "active"
        }
    
    @staticmethod
    def generate_order(user_id, cart_id, items):
        return {
            "userId": user_id,
            "cartId": cart_id,
            "items": items,
            "total": sum(i["priceAtPurchase"] * i["quantity"] for i in items),
            "status": "pending",
            "shippingAddress": fake.address(),
            "paymentMethod": fake.random_element(["credit_card", "paypal", "cod"])
        }
