# Vercel serverless function entry point for FastAPI
# This file is the entry point for Vercel's Python serverless functions

import os
import sys

# Add the chatkit-server directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables before importing main
from dotenv import load_dotenv
from pathlib import Path

repo_root = Path(__file__).resolve().parents[3]  # Go up to repo root
load_dotenv(repo_root / ".env")

from main import app

# Vercel expects the ASGI app to be available as `app`
# This is already imported from main.py