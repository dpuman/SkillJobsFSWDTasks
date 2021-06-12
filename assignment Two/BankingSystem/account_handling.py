# from user_account import UserAccount


# class Authentication(Exception):
#     pass


# class AccountHandler(UserAccount):

#     def __init__(self, name, password, balance, withdraw, deposit):
#         super(AccountHandler, self).__init__(
#             name, password, balance, withdraw, deposit)

#     def check_authentication(self, user_name, password, d_user, d_pass):
#         try:
#             if user_name != d_user or password != d_pass:
#                 raise Authentication

#             else:
#                 print(user_name, password, d_user, d_pass)
#                 self.balanceAccount()

#         except Exception:
#             print("Wrong user name or password")

#     def balanceAccount(self):
#         print("Balance")


# account = AccountHandler("Dipu", "1234", 1000, 100, 50)
# print(account.get_username(), account.get_password(), account.get_balance(),
#       account.get_withdraw(), account.get_deposit())

# d_user = account.get_username()
# d_pass = account.get_password()

# user_name = input("Please enter username:")
# password = input("Please enter password:")

# account.check_authentication(user_name, password, d_user, d_pass)
