#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "public"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

os.chdir(DIRECTORY)
print(f"🌐 Serving frontend at http://localhost:{PORT}")
print(f"📁 Open http://localhost:{PORT} in your browser")
print("📱 This frontend will connect to your Render API")
print("🚀 Press Ctrl+C to stop")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
