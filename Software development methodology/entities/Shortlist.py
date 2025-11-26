from database import database_management
import sqlite3, re
from entities.Request import Request 

class Shortlist:
    def __init__(self,shortlist_id=None, user_id=None, request_id=None):
        self.shortlist_id = shortlist_id
        self.user_id = user_id
        self.request_id = request_id

    
    def addToShortlist(self, request_id, csr_user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Check the request exists
        cursor.execute("""
            SELECT request_id
            FROM request
            WHERE request_id = ?
        """, (request_id,))
        row = cursor.fetchone()

        if row is None:
            conn.close()
            return None

        req_id = row["request_id"]

        # Optional: check duplicate
        cursor.execute("""
            SELECT 1 FROM shortlist
            WHERE user_id = ? AND request_id = ?
        """, (csr_user_id, req_id))
        exists = cursor.fetchone()
        if exists:
            conn.close()
            return "duplicate"

        # Insert into shortlist
        cursor.execute("""
            INSERT INTO shortlist (request_id, user_id)
            VALUES (?, ?)
        """, (req_id, csr_user_id))

        # **Increase shortlist count**
        cursor.execute("""
            UPDATE request
            SET request_shortlist_count = COALESCE(request_shortlist_count, 0) + 1
            WHERE request_id = ?
        """, (req_id,))

        conn.commit()
        conn.close()
        return True
        
    def searchShortlist(self, user_id, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        clean_keyword = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()
        cursor.execute("""
        SELECT 
            r.request_id,
            r.request_date,
            r.request_view_count,
            r.request_shortlist_count,
            r.request_status,
            r.category_id,
            c.category_name,
            c.category_desc
        FROM shortlist s
        JOIN request r ON r.request_id = s.request_id
        JOIN category c ON c.category_id = r.category_id
        WHERE s.user_id = ?
        AND LOWER(
            COALESCE(CAST(r.request_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.csrrep_user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.pin_user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.category_id AS TEXT), '') || ' ' ||
            COALESCE(r.request_status, '') || ' ' ||
            COALESCE(CAST(r.request_date AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_view_count AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_shortlist_count AS TEXT), '') || ' ' ||
            COALESCE(c.category_name, '') || ' ' ||
            COALESCE(c.category_desc, '')
        ) LIKE ?
        """,
        (user_id, f"%{clean_keyword}%"))
        rows = cursor.fetchall()
        conn.close()
        return [Request(**dict(row)) for row in rows] if rows else []
    
    def viewShortlist(self, csrrep_user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                r.request_id,
                r.request_date,
                r.request_view_count,
                r.request_shortlist_count,
                r.request_status,
                r.category_id,
                c.category_name,
                c.category_desc
            FROM shortlist s
            JOIN request r ON r.request_id = s.request_id
            JOIN category c ON c.category_id = r.category_id
            WHERE s.user_id = ?
        """, (csrrep_user_id,))

        rows = cursor.fetchall()
        conn.close()
        return [Request(**dict(row)) for row in rows] if rows else []
    

    def __str__(self):
        return (
        f"Shortlist(\n"
        f"  shortlist_id={self.shortlist_id},\n"
        f"  user_id={self.user_id},\n"
        f"  request_id={self.request_id}\n"
        f")"
    )
