This module checks for SQL Injection vulnerabilities by injecting common SQL payloads into query parameters and analyzing the server response for database error indicators.
SQL Injection is a High-risk OWASP Top 10 vulnerability and one of the most critical checks in AppSec assessments.
 
  import requests


class SQLiValidator:
    """
    Validator for detecting SQL Injection vulnerabilities.
    """

    def __init__(self, target_url: str):
        self.target_url = target_url

    def validate(self):
        findings = []
        payload = "' OR '1'='1"

        try:
            response = requests.get(
                self.target_url + "?id=" + payload,
                timeout=5
            )

            error_signatures = ["sql", "syntax", "mysql", "oracle", "postgres"]

            if any(err in response.text.lower() for err in error_signatures):
                findings.append({
                    "issue": "SQL Injection",
                    "severity": "High",
                    "url": self.target_url
                })

        except Exception:
            pass

        return findings
