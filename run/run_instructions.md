# Running WebGuardX AppSec Automation

This document explains how to execute the WebGuardX AppSec Automation Framework.

---

## Prerequisites
- Python 3.8 or higher
- Internet connectivity
- Permission to test the target application

---

## Installation

Install required dependencies:


pip install -r requirements.txt
Execution
Run the scanner using:
python appsec_runner.py
Enter the target URL when prompted.

Example:

arduino
http://testphp.vulnweb.com

Output
After execution, the security report is generated at:
reporting/appsec_report.txt
