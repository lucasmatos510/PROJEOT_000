#!/usr/bin/env python3
"""
WSGI entry point for WADE COLETOR
Optimized for production deployment on Render
"""

import os
import sys

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not available, using system environment variables")

# Import Flask app
try:
    from app import app
    print("✅ WADE COLETOR loaded successfully for production")
    print(f"🔐 SECRET_KEY configured: {bool(os.environ.get('SECRET_KEY'))}")
    print(f"🌍 Environment: {os.environ.get('FLASK_ENV', 'production')}")
except Exception as e:
    print(f"❌ Error loading app: {e}")
    raise

# For Gunicorn
application = app

if __name__ == "__main__":
    # For direct execution (development)
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    
    print(f"� Starting WADE COLETOR on {host}:{port}")
    app.run(host=host, port=port, debug=debug)