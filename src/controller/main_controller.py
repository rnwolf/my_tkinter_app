from src.model.app_model import AppModel
from src.view.main_view import MainView

class MainController:
    def __init__(self):
        self.model = AppModel()
        self.view = MainView(self)

    def run(self):
        self.view.mainloop()

    def update_model(self, data):
        self.model.update_data(data)
        self.view.update_view(self.model.get_data())
