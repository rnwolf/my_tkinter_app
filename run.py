#!/usr/bin/env python3
"""
Task Resource Manager - Entry point script

This script runs the Task Resource Manager application.
"""

import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.app import main

if __name__ == "__main__":
    main()