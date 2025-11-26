from database import database_management
import sqlite3
import re

class UserProfile:
    def __init__(self, role_id=None, role_name=None, description=None, status=None):
        self.role_id = role_id
        self.role_name = role_name
        self.description = description
        self.status = status
    
    def createProfile(self, role_name, description):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        # Check if role name already exists
        cursor.execute("SELECT role_name FROM userprofile WHERE role_name = ?", (role_name,))
        existing_profile = cursor.fetchone()
        if existing_profile:
            conn.close()
            return False  # Profile already exists
        cursor.execute("INSERT INTO userprofile (role_name, description, status) VALUES (?, ?, ?)", (role_name, description, 1))
        conn.commit()
        conn.close()
        return True 
    
    def ViewProfile(self):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM userprofile")
        rows = cursor.fetchall()
        conn.close()
        return [UserProfile(**dict(row)) for row in rows] if rows else []
    
    def updateProfile(self, role_id, role_name, description):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        # Check if role name already exists
        cursor.execute("SELECT role_id FROM userprofile WHERE role_name = ? AND role_id != ?", (role_name, role_id))
        existing_profile = cursor.fetchone()
        if existing_profile:
            conn.close()
            return False  # Profile already exists
        cursor.execute("UPDATE userprofile SET role_name = ?, description = ? WHERE role_id = ?", (role_name, description, role_id,))
        conn.commit()
        conn.close()
        return True
    
    def suspendProfile(self, role_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if role_id == '1':
            conn.close()
            return False
        cursor.execute("UPDATE userprofile SET status = false WHERE role_id = ?", (role_id,))
        conn.commit()
        conn.close()
        return True
    
    def reactivateProfile(self, role_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE userprofile SET status = true WHERE role_id = ?", (role_id,))
        conn.commit()
        conn.close()
        return True
    
    def searchProfile(self, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        clean_term = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()

        cursor.execute("""
            SELECT role_id, role_name, description, status
            FROM userprofile
            WHERE LOWER(role_name) LIKE ?
            OR LOWER(description) LIKE ?
        """, (
            f"%{clean_term}%",
            f"%{clean_term}%"
        ))

        rows = cursor.fetchall()
        conn.close()

        return [UserProfile(**dict(row)) for row in rows] if rows else []

    def getProfileById(self, role_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM userprofile WHERE role_id = ?", (role_id,))
        role = cursor.fetchone()
        conn.close()

        return role  # This returns a Row object or None if not found
    
    def __str__(self):
        return (f"UserProfile(\n"
            f"  role_id={self.role_id},\n"
            f"  role_name={self.role_name},\n"
            f"  description={self.description},\n"
            f"  status={self.status},\n"
            f")")
