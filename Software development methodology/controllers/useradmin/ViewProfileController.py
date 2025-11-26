from entities.UserProfile import UserProfile    

class ViewProfileController:
    def __init__(self):
        pass
    
    def ViewProfile(self):
        user_profile = UserProfile()
        return user_profile.ViewProfile()
