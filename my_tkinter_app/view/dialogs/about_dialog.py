# my_tkinter_app/view/dialogs/about_dialog.py
import tkinter as tk
from tkinter import ttk
from my_tkinter_app import __version__, __author__, __release_date__


class AboutDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('About')
        self.resizable(False, False)
        self.transient(parent)  # Make dialog a child of parent

        # Make dialog modal
        self.grab_set()  # Prevent interaction with the parent window

        # Center the dialog relative to parent
        window_width = 300
        window_height = 200

        # Calculate position x, y
        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()

        x = parent_x + (parent_width - window_width) // 2
        y = parent_y + (parent_height - window_height) // 2

        # Set geometry
        self.geometry(f'{window_width}x{window_height}+{x}+{y}')

        self.create_widgets()

        # Wait for the dialog to be closed before returning control
        self.wait_visibility()
        self.focus_set()

    def create_widgets(self):
        frame = ttk.Frame(self, padding='20')
        frame.pack(fill=tk.BOTH, expand=True)

        # Application info
        ttk.Label(
            frame, text='MVC Tkinter App', font=('TkDefaultFont', 12, 'bold')
        ).pack(pady=(0, 10))
        ttk.Label(frame, text=f'Version: {__version__}').pack(anchor=tk.W)
        ttk.Label(frame, text=f'Author: {__author__}').pack(anchor=tk.W)
        ttk.Label(frame, text=f'Release Date: {__release_date__}').pack(anchor=tk.W)

        # Close button
        ttk.Button(frame, text='Close', command=self.destroy).pack(pady=(20, 0))

    # Add to the AboutDialog class
    def destroy(self):
        # Release grab before destroying
        self.grab_release()
        super().destroy()