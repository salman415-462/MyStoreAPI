import requests
import time
import subprocess
import sys

print("🔍 Testing MyStore API Setup...")

# Check if db.json exists
import os
if not os.path.exists('db.json'):
    print("❌ db.json not found! Creating it...")
    with open('db.json', 'w') as f:
        f.write('{"products": [], "users": [], "carts": [], "orders": []}')

print("1. Starting json-server...")
try:
    # Start server without --quiet flag
    server = subprocess.Popen(
        ['json-server', '--watch', 'db.json', '--port', '3000'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(3)
    
    print("2. Testing API endpoints...")
    
    # Test products endpoint
    r = requests.get('http://localhost:3000/products', timeout=5)
    print(f"   GET /products: {r.status_code}")
    
    if r.status_code == 200:
        data = r.json()
        print(f"   Found {len(data)} products")
        
        # Test POST if no products
        if len(data) == 0:
            new_product = {
                "name": "Test Laptop",
                "price": 999.99,
                "category": "electronics"
            }
            r = requests.post('http://localhost:3000/products', json=new_product, timeout=5)
            print(f"   POST /products: {r.status_code}")
    
    print("\n✅ All basic tests passed!")
    
except requests.exceptions.ConnectionError:
    print("❌ Cannot connect to API. Make sure json-server is installed.")
    print("   Install with: npm install -g json-server")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    # Cleanup
    if 'server' in locals():
        print("\n3. Stopping server...")
        server.terminate()
        server.wait()

print("\n🎯 Setup complete! Run './run_tests.sh' for full test suite")
