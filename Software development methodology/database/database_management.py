import sqlite3


def dbConnection():
    return sqlite3.connect("database/volunteer_system.db")

def userProfileTableSetup():
    conn = dbConnection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS userprofile")
    profile_data = open("database/mock-data/userprofile.sql", "r")
    profile_sql = profile_data.read()
    profile_data.close()
    profile_sql_cmds = profile_sql.split(";")
    for sql in profile_sql_cmds:
        try:
            cursor.execute(sql)
        except Exception as err:
            print("Skipped: ", err)
    print("User profile table has been created successfully!")
    conn.commit()

def userTableSetup():
    conn = dbConnection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS user")
    user_data = open("database/mock-data/user.sql", "r")
    user_sql = user_data.read()
    user_data.close()
    user_sql_cmds = user_sql.split(";")
    for sql in user_sql_cmds:
        try:
            cursor.execute(sql)
        except Exception as err:
            print("Skipped: ", err)
    print("User table has been created successfully!")
    conn.commit()

def categoryTableSetup():
    conn = dbConnection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS category")
    category_data = open("database/mock-data/category.sql", "r")
    category_sql = category_data.read()
    category_data.close()
    category_sql_cmds = category_sql.split(";")
    for sql in category_sql_cmds:
        try:
            cursor.execute(sql)
        except Exception as err:
            print("Skipped: ", err)
    print("Category table has been created successfully!")
    conn.commit()

def requestTableSetup():
    conn = dbConnection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS request")
    request_data = open("database/mock-data/request.sql", "r")
    request_sql = request_data.read()
    request_data.close()
    request_sql_cmds = request_sql.split(";")
    for sql in request_sql_cmds:
        try:
            cursor.execute(sql)
        except Exception as err:
            print("Skipped: ", err)
    print("Request table has been created successfully!")
    conn.commit()

def shortlistTableSetup():
    conn = dbConnection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS shortlist")
    shortlist_data = open("database/mock-data/shortlist.sql", "r")
    shortlist_sql = shortlist_data.read()
    shortlist_data.close()
    shortlist_sql_cmds = shortlist_sql.split(";")
    for sql in shortlist_sql_cmds:
        try:
            cursor.execute(sql)
        except Exception as err:
            print("Skipped: ", err)
    print("Shortlist table has been created successfully!")
    conn.commit()


# For Debugging Purposes
def getUser(email, password):
    conn = dbConnection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE email = ? AND password = ?", (email, password))
    query_result = cursor.fetchone()
    conn.close()
    if query_result != None:
        return dict(query_result)
    return None


# Testing Purposes
if __name__ == "__main__":
    print("\n")
    userProfileTableSetup()
    userTableSetup()
    categoryTableSetup()
    requestTableSetup()
    shortlistTableSetup()
    print("\n\nAll tables have been created successfully!")
    print("\n")
    # print(getUser("latisha.brandle@volunteer.com", "password123")) # CSR Rep
    # print(getUser("rhonda.bonnet@volunteer.com", "password123")) # PM
    # print(getUser("kirsteni.demcik@volunteer.com", "password123")) # PIN
    # print(getUser("lawton.korfmann@volunteer.com", "password123")) # UserAdmin


