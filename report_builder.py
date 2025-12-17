The reporting layer consolidates vulnerability findings and generates a structured AppSec report that can be shared with development or security teams.

from datetime import datetime


class ReportBuilder:
    """
    Responsible for generating structured security reports
    from AppSec vulnerability findings.
    """

    def __init__(self, findings: list):
        """
        Initialize the report builder.

        :param findings: List of vulnerability findings
        """
        self.findings = findings

    def build(self):
        """
        Generate a text-based AppSec security report.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report_path = "reporting/appsec_report.txt"

        with open(report_path, "w") as report:
            report.write("WebGuardX – Application Security Report\n")
            report.write(f"Generated On: {timestamp}\n")
            report.write("=" * 50 + "\n\n")

            if not self.findings:
                report.write("No vulnerabilities detected.\n")
            else:
                for item in self.findings:
                    report.write(f"Issue     : {item.get('issue')}\n")
                    report.write(f"Severity  : {item.get('severity')}\n")
                    report.write(f"URL       : {item.get('url')}\n")

                    if "details" in item:
                        report.write(f"Details   : {item.get('details')}\n")

                    report.write("-" * 50 + "\n")

        print(f"[+] Security report generated at: {report_path}")
