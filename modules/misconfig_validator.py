import requests


class MisconfigValidator:
    """
    Validator for detecting common security misconfigurations
    such as exposed administrative interfaces or unsecured endpoints.
    """

    def __init__(self, target_url: str):
        """
        Initialize the validator with the target application URL.

        :param target_url: Web application base URL
        """
        self.target_url = target_url

    def validate(self):
        """
        Perform security misconfiguration checks.

        :return: List of identified misconfiguration findings
        """
        findings = []

        # Common sensitive paths checked during AppSec assessments
        sensitive_paths = [
            "/admin",
            "/dashboard",
            "/config",
            "/phpinfo.php"
        ]

        for path in sensitive_paths:
            try:
                response = requests.get(
                    self.target_url + path,
                    timeout=5
                )

                if response.status_code == 200:
                    findings.append({
                        "issue": "Security Misconfiguration",
                        "severity": "Low",
                        "url": self.target_url + path,
                        "details": f"Exposed endpoint detected at {path}"
                    })

            except Exception:
                # Ignore connection errors to avoid scan interruption
                pass

        return findings
