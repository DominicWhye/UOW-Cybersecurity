from entities.UserAccount import UserAccount

class UpdateUserAccController:
    def __init__(self):
        pass

    def getUserById(self, user_id):
        user = UserAccount()
        return user.getUserById(user_id)

    def updateUser(self, user_id, email, password, role_id, first_name, last_name, address, phone):
        user_account = UserAccount(
            user_id=user_id,
            role_id=role_id,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            created_at=None
        )
        return user_account.updateUser(user_id, email, password, role_id, first_name, last_name, address, phone)