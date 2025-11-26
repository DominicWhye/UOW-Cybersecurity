from entities.Report import Report

class GenerateMonthlyReportController:
    @staticmethod
    def generateMonthlyReport(year_month: str, limit: int | None = None):
        """
        Generates the monthly report for the specified month (YYYY-MM format).
        """
        report = Report()
        return report.generateMonthlyReport(year_month=year_month, limit=limit)