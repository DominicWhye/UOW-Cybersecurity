from entities.UserAccount import UserAccount

class SuspendUserAccController:
    def __init__(self,user_id):
        self.user_id = user_id
    
    def suspendUser(self,user_id):
        user_account = UserAccount(
            user_id=user_id,
            role_id=None,
            email=None,
            password=None,
            first_name=None,
            last_name=None,
            address=None,
            phone=None,
            is_active=None,
            created_at=None
        )
        return user_account.suspendUser(user_id)