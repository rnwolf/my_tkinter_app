# my_tkinter_app/view/components/status_bar.py
import tkinter as tk
from tkinter import ttk


class StatusBar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief=tk.SUNKEN)
        self.status_var = tk.StringVar()
        self.status_var.set('Ready')

        self.label = ttk.Label(self, textvariable=self.status_var, anchor=tk.W)
        self.label.pack(fill=tk.X, padx=5, pady=2)

    def set_status(self, text):
        """Update the status bar text"""
        self.status_var.set(text)