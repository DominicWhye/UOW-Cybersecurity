from entities.UserProfile import UserProfile

class SearchProfileController:
    def __init__(self):
        self.user_profile = UserProfile()
    
    def searchProfile(self, keyword):
        return self.user_profile.searchProfile(keyword)