class Endpoints:
    BASE_URL = "http://localhost:3000"
    
    # Products endpoints
    PRODUCTS = f"{BASE_URL}/products"
    PRODUCT_BY_ID = PRODUCTS + "/{id}"
    PRODUCTS_BY_CATEGORY = PRODUCTS + "?category={category}"
    
    # Users endpoints
    USERS = f"{BASE_URL}/users"
    USER_BY_ID = USERS + "/{id}"
    
    # Carts endpoints
    CARTS = f"{BASE_URL}/carts"
    CART_BY_ID = CARTS + "/{id}"
    USER_CARTS = CARTS + "?userId={userId}"
    
    # Orders endpoints
    ORDERS = f"{BASE_URL}/orders"
    ORDER_BY_ID = ORDERS + "/{id}"
    USER_ORDERS = ORDERS + "?userId={userId}"
