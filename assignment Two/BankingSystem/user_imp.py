from abstractor import User


class UserImp(User):

    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    def get_username(self):
        return self.__name

    def set_username(self, name):
        self.__name = name

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password
