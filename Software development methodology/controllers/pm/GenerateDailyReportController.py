from entities.Report import Report

class GenerateDailyReportController:
    @staticmethod
    def generateDailyReport(report_date: str, limit: int | None = None):
        """
        Generates the daily report for the specified date (YYYY-MM-DD).
        """
        report = Report()
        return report.generateDailyReport(report_date=report_date, limit=limit)
