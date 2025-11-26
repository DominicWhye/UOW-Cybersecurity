# entities/Report.py
from database import database_management
import sqlite3
from typing import List, Dict, Optional

class Report:
    """Generate popular-category reports."""

    def generateDailyReport(self, report_date: str, limit: Optional[int] = None) -> List[Dict]:
        if not report_date:
            raise ValueError("report_date (YYYY-MM-DD) is required for daily report.")

        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        date_iso = (
            "CASE "
            "WHEN r.request_date LIKE '____-__-__' THEN r.request_date "
            "WHEN r.request_date LIKE '__/__/____' THEN "
            "substr(r.request_date,7,4) || '-' || substr(r.request_date,4,2) || '-' || substr(r.request_date,1,2) "
            "ELSE NULL END"
        )

        sql = f"""
            SELECT
                c.category_id,
                c.category_name,
                c.category_desc,
                COUNT(r.request_id) AS total_requests,
                COALESCE(SUM(r.request_shortlist_count), 0) AS total_shortlists,
                COALESCE(SUM(r.request_view_count), 0) AS total_views
            FROM category c
            LEFT JOIN request r ON c.category_id = r.category_id
            WHERE DATE({date_iso}) = DATE(?)
            GROUP BY c.category_id
            ORDER BY total_views DESC, total_shortlists DESC, total_requests DESC
        """

        if limit and isinstance(limit, int) and limit > 0:
            sql += " LIMIT ?"
            cur.execute(sql, (report_date, limit))
        else:
            cur.execute(sql, (report_date,))

        rows = cur.fetchall()
        conn.close()
        return [dict(r) for r in rows] if rows else []

    def generateWeeklyReport(self, start_date: str, limit: Optional[int] = None) -> List[Dict]:
        if not start_date:
            raise ValueError("start_date (YYYY-MM-DD) is required for weekly report.")

        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        date_iso = (
            "CASE "
            "WHEN r.request_date LIKE '____-__-__' THEN r.request_date "
            "WHEN r.request_date LIKE '__/__/____' THEN "
            "substr(r.request_date,7,4) || '-' || substr(r.request_date,4,2) || '-' || substr(r.request_date,1,2) "
            "ELSE NULL END"
        )

        sql = f"""
            SELECT
                c.category_id,
                c.category_name,
                c.category_desc,
                COUNT(r.request_id) AS total_requests,
                COALESCE(SUM(r.request_shortlist_count), 0) AS total_shortlists,
                COALESCE(SUM(r.request_view_count), 0) AS total_views
            FROM category c
            LEFT JOIN request r ON c.category_id = r.category_id
            WHERE DATE({date_iso}) BETWEEN DATE(?) AND DATE(?, '+6 days')
            GROUP BY c.category_id
            ORDER BY total_views DESC, total_shortlists DESC, total_requests DESC
        """

        if limit and isinstance(limit, int) and limit > 0:
            sql += " LIMIT ?"
            cur.execute(sql, (start_date, start_date, limit))
        else:
            cur.execute(sql, (start_date, start_date))

        rows = cur.fetchall()
        conn.close()
        return [dict(r) for r in rows] if rows else []

    def generateMonthlyReport(self, year_month: str, limit: Optional[int] = None) -> List[Dict]:
        if not year_month:
            raise ValueError("year_month (YYYY-MM) is required for monthly report.")

        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        date_iso = (
            "CASE "
            "WHEN r.request_date LIKE '____-__-__' THEN r.request_date "
            "WHEN r.request_date LIKE '__/__/____' THEN "
            "substr(r.request_date,7,4) || '-' || substr(r.request_date,4,2) || '-' || substr(r.request_date,1,2) "
            "ELSE NULL END"
        )

        sql = f"""
            SELECT
                c.category_id,
                c.category_name,
                c.category_desc,
                COUNT(r.request_id) AS total_requests,
                COALESCE(SUM(r.request_shortlist_count), 0) AS total_shortlists,
                COALESCE(SUM(r.request_view_count), 0) AS total_views
            FROM category c
            LEFT JOIN request r ON c.category_id = r.category_id
            WHERE strftime('%Y-%m', {date_iso}) = ?
            GROUP BY c.category_id
            ORDER BY total_views DESC, total_shortlists DESC, total_requests DESC
        """

        if limit and isinstance(limit, int) and limit > 0:
            sql += " LIMIT ?"
            cur.execute(sql, (year_month, limit))
        else:
            cur.execute(sql, (year_month,))

        rows = cur.fetchall()
        conn.close()
        return [dict(r) for r in rows] if rows else []
