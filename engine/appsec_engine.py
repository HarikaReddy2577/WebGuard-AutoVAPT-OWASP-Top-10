In real-world AppSec tools, the engine is responsible for:

Coordinating multiple security checks
Controlling scan flow
Aggregating results from different vulnerability modules
Triggering report generation
This file does not perform attacks directly.
Instead, it manages and executes validation modules in a structured and scalable way.

RESPONSIBILITIES OF AppSecEngine
  
  Accept target URL
Invoke OWASP Top 10 validators
Collect vulnerability findings
Send results to report generator
Maintain clean execution flow

  from modules.sqli_validator import SQLiValidator
from modules.xss_validator import XSSValidator
from modules.auth_validator import AuthValidator
from modules.misconfig_validator import MisconfigValidator
from reporting.report_builder import ReportBuilder


class AppSecEngine:
    """
    AppSecEngine is the core orchestration layer of the WebGuardX framework.

    It coordinates the execution of multiple OWASP Top 10 vulnerability
    validators, aggregates their findings, and triggers report generation.
    """

    def __init__(self, target_url: str):
        """
        Initialize the AppSec engine with a target application URL.

        :param target_url: Web application URL to be tested
        """
        self.target_url = target_url
        self.findings = []

    def execute(self):
        """
        Execute the full Application Security scan.

        This method runs all vulnerability validators in sequence,
        collects findings, and generates a consolidated report.
        """
        print("[+] Starting Application Security Scan")
        print(f"[+] Target: {self.target_url}")

        # Execute vulnerability checks
        self.findings.extend(SQLiValidator(self.target_url).validate())
        self.findings.extend(XSSValidator(self.target_url).validate())
        self.findings.extend(AuthValidator(self.target_url).validate())
        self.findings.extend(MisconfigValidator(self.target_url).validate())

        # Generate report
        ReportBuilder(self.findings).build()

        print("[+] Application Security Scan Completed")
