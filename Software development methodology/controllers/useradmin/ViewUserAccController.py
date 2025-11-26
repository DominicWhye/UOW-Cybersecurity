from entities.UserAccount import UserAccount

class ViewUserAccController:
    def __init__(self):
        self.user_account = UserAccount()
    
    def viewUser(self):
        return self.user_account.viewUser()