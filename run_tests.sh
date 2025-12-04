#!/bin/bash
echo "🧪 Running MyStore API Tests..."
echo "================================"

# Start json-server in background
echo "1. Starting json-server..."
json-server --watch db.json --port 3000 > /dev/null 2>&1 &
SERVER_PID=$!

# Wait for server to start
sleep 3
echo "2. Server started on http://localhost:3000"

echo "3. Running tests..."
python3 -m pytest tests/ -v --html=report.html

echo "4. Stopping json-server..."
kill $SERVER_PID 2>/dev/null

echo "✅ Tests completed!"
echo "📊 Report generated: report.html"
echo ""
echo "🎯 To view report:"
echo "   Open 'report.html' in your browser"
