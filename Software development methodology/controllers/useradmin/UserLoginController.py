from entities.UserAccount import UserAccount

class UserLoginController:
    def login(email, password):
        user_account = UserAccount()
        return user_account.login(email, password)