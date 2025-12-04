#!/bin/bash
echo "🚀 Starting MyStore API on http://localhost:3000"
echo ""
echo "📊 Available endpoints:"
echo "   http://localhost:3000/products"
echo "   http://localhost:3000/users"
echo "   http://localhost:3000/carts"
echo "   http://localhost:3000/orders"
echo ""
json-server --watch db.json --port 3000
