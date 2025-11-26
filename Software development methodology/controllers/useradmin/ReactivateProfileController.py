from entities.UserProfile import UserProfile

class ReactivateProfileController:
    def __init__(self):
        pass

    def reactivateProfile(self, role_id):
        user_profile = UserProfile(
            role_id=None,
            role_name=None,
            description=None,
            status=None
        )
        return user_profile.reactivateProfile(role_id)