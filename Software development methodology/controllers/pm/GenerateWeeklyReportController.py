from entities.Report import Report

class GenerateWeeklyReportController:
    @staticmethod
    def generateWeeklyReport(start_date: str, limit: int | None = None):
        """
        Generates the weekly report for a 7-day window starting from the specified date (YYYY-MM-DD).
        """
        report = Report()
        return report.generateWeeklyReport(start_date=start_date, limit=limit)