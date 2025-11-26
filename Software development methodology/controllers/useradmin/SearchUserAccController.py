from entities.UserAccount import UserAccount

class SearchUserAccController:
    def __init__(self):
        self.user_account = UserAccount()
    
    def searchUser(self, keyword):
        return self.user_account.searchUser(keyword)