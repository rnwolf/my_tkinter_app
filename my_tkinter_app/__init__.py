"""
A Tkinter application
"""

__version__ = "0.1.1"
__author__ = 'R.N. Wolf'
__release_date__ = "2025-04-03"

from my_tkinter_app.controller import main_controller
from my_tkinter_app.model import app_model
from my_tkinter_app.view import main_view

__all__ = {
    'main_view',
    'main_controller',
    'app_model',
}
