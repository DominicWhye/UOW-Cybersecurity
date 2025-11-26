from entities.UserProfile import UserProfile

class CreateProfileController:
    def __init__(self):
        pass

    def createProfile(self, role_name, description):
        user_profile = UserProfile(
            role_name=role_name,
            description=description
        )
        return user_profile.createProfile(role_name, description)
    
    