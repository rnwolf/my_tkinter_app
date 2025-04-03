import tkinter as tk

class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("MVC Tkinter App")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Hello, Tkinter!")
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Update Model", command=self.on_button_click)
        self.button.pack(pady=20)

    def on_button_click(self):
        new_data = {"message": "Model Updated!"}
        self.controller.update_model(new_data)

    def update_view(self, data):
        self.label.config(text=data.get("message", "No data"))
