# my_tkinter_app/view/components/main_frame.py
import tkinter as tk
from tkinter import ttk


class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding='10')

        # Sample content
        self.label = ttk.Label(self, text='Main Content Area')
        self.label.pack(pady=50)

        # Add more widgets as needed