from my_tkinter_app.model.app_model import AppModel
from my_tkinter_app.view.main_view import MainView

class MainController:
    def __init__(self):
        self.model = AppModel()
        self.view = MainView(self)

    def run(self):
        self.view.mainloop()

    def update_model(self, data):
        self.model.update_data(data)
        self.view.update_view(self.model.get_data())
