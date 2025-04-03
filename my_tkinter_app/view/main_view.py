# my_tkinter_app/view/main_view.py
import tkinter as tk
from tkinter import ttk

from my_tkinter_app.view.components.status_bar import StatusBar
from my_tkinter_app.view.components.main_frame import MainFrame
from my_tkinter_app.view.menus.main_menu import MainMenu


class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('MVC Tkinter App')
        self.geometry('600x400')

        # Configure the grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # Menu Bar
        self.menu_bar = MainMenu(self, self.controller)
        self.config(menu=self.menu_bar)

        # Main Frame (content area)
        self.main_frame = MainFrame(self)
        self.main_frame.grid(row=0, column=0, sticky='nsew')

        # Status Bar
        self.status_bar = StatusBar(self)
        self.status_bar.grid(row=1, column=0, sticky='ew')

    def update_view(self, data):
        """Update the view based on model data"""
        message = data.get('message', 'No data')
        self.main_frame.label.config(text=message)
        self.status_bar.set_status(f"Last update: {message}")