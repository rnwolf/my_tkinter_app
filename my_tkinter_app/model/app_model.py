class AppModel:
    def __init__(self):
        self.data = {}

    def update_data(self, data):
        self.data.update(data)

    def get_data(self):
        return self.data
