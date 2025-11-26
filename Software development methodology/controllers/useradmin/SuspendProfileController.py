from entities.UserProfile import UserProfile

class SuspendProfileController:
    def __init__(self):
        pass
    
    def suspendProfile(self, role_id):
        user_profile = UserProfile(
            role_id=role_id,
            role_name=None,
            description=None,
            status=None
        )
        return user_profile.suspendProfile(role_id)