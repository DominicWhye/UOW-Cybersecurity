from entities.UserAccount import UserAccount

if __name__ == "__main__":
    user_acct = UserAccount()
    accounts = user_acct.viewUser()
    for account in accounts:
        print(account.first_name)