from entities.UserAccount import UserAccount

class CreateUserAccController:
    def __init__(self):
        pass

    def createUser(self, role_id, email, password, first_name, last_name, address, phone):
        user_account = UserAccount(
            role_id=role_id,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            is_active=1,
            created_at=None
        )

        return user_account.createUser(role_id, email, password, first_name, last_name, address, phone)
