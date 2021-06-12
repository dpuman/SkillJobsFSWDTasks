from user_imp import UserImp


class Authentication(Exception):
    pass


class UserAccount(UserImp):

    def __init__(self, name, password, balance, withdraw, deposit):
        super(UserAccount, self).__init__(name, password)
        self.__balance = balance
        self.__withdraw = withdraw
        self.__deposit = deposit

    def set_balance(self, balance): self.__balance = balance

    def get_balance(self): return self.__balance

    def set_withdraw(self, withdraw): self.__withdraw = withdraw

    def get_withdraw(self): return self.__withdraw

    def set_deposit(self, deposit): self.__deposit = deposit

    def get_deposit(self): return self.__deposit

    def check_authentication(self, user_name, password, d_user, d_pass):
        try:
            if user_name != d_user or password != d_pass:
                raise Authentication

            else:
                print(user_name, password, d_user, d_pass)
                self.balanceAccount()

        except Exception:
            print("Wrong user name or password")

    def balanceAccount(self):
        print("Your Balance is :", self.__balance)

        withdraw = int(input("Give your withdraw amount: "))
        deposite = int(input("Give your deposite amount: "))

        self.__balance -= withdraw
        self.__balance += deposite

        print("Your New balance is :", self.__balance)


account = UserAccount("Dipu", "1234", 1000, 100, 50)
print(account.get_username(), account.get_password(), account.get_balance(),
      account.get_withdraw(), account.get_deposit())

d_user = account.get_username()
d_pass = account.get_password()

user_name = input("Please enter username:")
password = input("Please enter password:")

account.check_authentication(user_name, password, d_user, d_pass)
