"""
A Tkinter application
"""

__version__ = "0.1.0"
__author__ = 'R.N. Wolf'
__release_date__ = "2025-04-03"

from src.controller import main_controller
from src.model import app_model
from src.view import main_view

__all__ = {
    'main_view',
    'main_controller',
    'app_model',
}
