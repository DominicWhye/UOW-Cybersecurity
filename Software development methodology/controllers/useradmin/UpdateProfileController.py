from entities.UserProfile import UserProfile    

class UpdateProfileController:
    def __init__(self):
        pass
    
    def getProfileById(self, user_id):
        profile = UserProfile()
        return profile.getProfileById(user_id)

    def updateProfile(self, role_id, role_name, description):
        user_profile = UserProfile(
            role_id=role_id,
            role_name=role_name,
            description=description,
        )
        return user_profile.updateProfile(role_id, role_name, description)