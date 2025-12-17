This module detects Cross-Site Scripting (XSS) by injecting JavaScript payloads and checking whether they are reflected unescaped in the response.
XSS is a client-side vulnerability that can lead to session hijacking and data theft.

import requests


class XSSValidator:
    """
    Validator for detecting reflected Cross-Site Scripting (XSS).
    """

    def __init__(self, target_url: str):
        self.target_url = target_url

    def validate(self):
        findings = []
        payload = "<script>alert('XSS')</script>"

        try:
            response = requests.get(
                self.target_url + "?q=" + payload,
                timeout=5
            )

            if payload in response.text:
                findings.append({
                    "issue": "Cross-Site Scripting (XSS)",
                    "severity": "Medium",
                    "url": self.target_url
                })

        except Exception:
            pass

        return findings
