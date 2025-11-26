from database import database_management
import sqlite3
from datetime import datetime
import re

class UserAccount:
    def __init__(self, user_id=None, role_id=None, email=None, password=None, first_name=None, last_name=None, 
                 address=None, phone=None, is_active=None, created_at=None):
        self.user_id = user_id
        self.role_id = role_id 
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.is_active = is_active
        self.created_at = created_at

    def login(self, email, password):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE email = ? AND password = ?", (email, password))
        query_result = cursor.fetchone()
        conn.close()
        if query_result is None:
            return None
        
        accounts_db = dict(query_result)
        # Check if user account exists, hardcoded for testing purposes
        # Role ID for UserAdmin (1), PM (2), PIN (3), CSR Rep (4)
        if accounts_db and int(accounts_db["is_active"]) != 0:
            if accounts_db["email"] == email and accounts_db["password"] == password:
                return UserAccount (
                    user_id = accounts_db["user_id"], # Here we will return from DB according to email and password
                    role_id = accounts_db["role_id"],
                    password = accounts_db["password"],
                    email = accounts_db["email"],
                    first_name = accounts_db["first_name"],
                    last_name = accounts_db["last_name"],
                    address = accounts_db["address"],
                    phone = accounts_db["phone"],
                    is_active = accounts_db["is_active"],
                    created_at = accounts_db["created_at"]
                )
        return None
    
    def createUser(self, role_id, email, password, first_name, last_name, address, phone):
        conn = database_management.dbConnection()
        cursor = conn.cursor()
        
        # Check if email already exists
        cursor.execute("SELECT email FROM user WHERE email = ?", (email,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            conn.close()
            return False  # Email already exists
        
        # Email doesn't exist already, proceed with creation
        created_at = datetime.now().strftime('%d/%m/%Y')
        
        cursor.execute("""
            INSERT INTO user (
                role_id, first_name, last_name, email, password, address, phone, is_active, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            role_id,       # <-- must be first
            first_name,
            last_name,
            email,
            password,
            address,
            phone,
            True,
            created_at
        ))


        conn.commit()
        conn.close()
        return True  # User created successfully    

    def viewUser(self):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        conn.close()
        return [UserAccount(**dict(row)) for row in rows] if rows else []
    
    def updateUser(self, user_id, email, password, role_id, first_name, last_name, address, phone):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Check if email already exists for a different user
        cursor.execute("SELECT user_id FROM user WHERE email = ? AND user_id != ?", (email, user_id))
        existing_user = cursor.fetchone()
        if existing_user:
            conn.close()
            return False  # Email already exists for another user

        # Update password only if provided; otherwise keep existing password
        if password:
            cursor.execute("""
                UPDATE user SET email = ?, password = ?, role_id = ?, first_name = ?, last_name = ?, address = ?, phone = ? WHERE user_id = ?
            """, (email, password, role_id, first_name, last_name, address, phone, user_id))
        else:
            # Exclude password if not changed
            cursor.execute("""
                UPDATE user SET email = ?, role_id = ?, first_name = ?, last_name = ?, address = ?, phone = ? WHERE user_id = ?
            """, (email, role_id, first_name, last_name, address, phone, user_id))

        conn.commit()
        conn.close()
        return True


    def suspendUser(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE user SET is_active = 0 WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
        return True
    
    def reactivateUser(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE user SET is_active = 1 WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
        return True

    def searchUser(self, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        clean_term = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()
        cursor.execute("""
            SELECT user_id, role_id, email, password, first_name, last_name, 
                address, phone, is_active, created_at
            FROM user
            WHERE LOWER(first_name) LIKE ?
            OR LOWER(last_name) LIKE ?
            OR LOWER(email) LIKE ?
            OR LOWER(phone) LIKE ?
            OR LOWER(first_name || ' ' || last_name) LIKE ?
            OR LOWER(REPLACE(REPLACE(email, '.', ''), '@', '')) LIKE ?
        """, (
            f"%{clean_term}%",
            f"%{clean_term}%",
            f"%{clean_term}%",
            f"%{clean_term}%",
            f"%{clean_term}%",
            f"%{clean_term}%"
        ))
        rows = cursor.fetchall()
        conn.close()
        return [UserAccount(**dict(row)) for row in rows] if rows else []
    
    def getUserById(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()

        return user  # This returns a Row object or None if not found
    
    def __str__(self):
        return (f"UserAccount(\n"
            f"  user_id={self.user_id},\n"
            f"  role_id={self.role_id},\n"
            f"  email={self.email},\n"
            f"  password={self.password},\n"
            f"  first_name={self.first_name},\n"
            f"  last_name={self.last_name},\n"
            f"  address={self.address},\n"
            f"  phone={self.phone},\n"
            f"  is_active={self.is_active},\n"
            f"  created_at={self.created_at}\n"
            f")")