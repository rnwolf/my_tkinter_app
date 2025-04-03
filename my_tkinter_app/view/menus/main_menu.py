# my_tkinter_app/view/menus/main_menu.py
import tkinter as tk
from my_tkinter_app.view.dialogs.about_dialog import AboutDialog


class MainMenu(tk.Menu):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent

        # Create Help menu
        self.help_menu = tk.Menu(self, tearoff=0)
        self.help_menu.add_command(label='About', command=self.show_about_dialog)

        # Add menus to the menubar
        self.add_cascade(label='Help', menu=self.help_menu)

        # You can add more menus here (File, Edit, etc.)

    def show_about_dialog(self):
        """Display the About dialog"""
        dialog = AboutDialog(self.parent)
        self.parent.wait_window(dialog)  # Wait until dialog is closed makes the dialog truly modal, preventing interaction with the parent until the dialog is closed.