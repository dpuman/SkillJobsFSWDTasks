from abc import ABC


class User(ABC):
    def get_username(self):
        pass

    def set_username(self, name):
        pass

    def get_password(self):
        pass

    def set_password(self, password):
        pass
