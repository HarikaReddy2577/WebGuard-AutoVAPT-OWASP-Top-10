# 🛡️ WebGuardX – AppSec Automation Framework
### Automated Web Application Security Testing (OWASP Top 10)

**WebGuardX-AppSec-Automation** is a Python-based **Application Security (AppSec) automation tool** designed to detect common **OWASP Top 10 vulnerabilities** using a modular and real-world architecture.

---

## 📌 Overview
WebGuardX simulates how real AppSec and VAPT tools operate by separating:
- Scan orchestration
- Vulnerability validation
- Reporting
- Configuration
- Execution logging

This project demonstrates **hands-on AppSec skills combined with software engineering best practices**.

---

## 🎯 Why I Built This
I built WebGuardX to move beyond theory and understand **how vulnerabilities are validated programmatically** and how **real AppSec tools are structured** in security teams.

---

## 🧠 Learning Outcomes
- OWASP Top 10 vulnerability analysis  
- Modular Python application design  
- Payload-based validation logic  
- Security report generation  
- Logging and execution tracking  
- Ethical security testing practices  

---

## 🔍 Vulnerabilities Covered
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)
- Broken Authentication
- Security Misconfiguration

---

## ✨ Key Features
✔ Modular vulnerability validators  
✔ Engine-based scan orchestration  
✔ Config-driven payload management  
✔ Structured security reports  
✔ Execution logs & proof screenshots  

---

## 🏗️ Project Structure
```text
WebGuardX-AppSec-Automation/
├── engine/        # Core scan engine
├── modules/       # OWASP validators
├── reporting/     # Report generation
├── config/        # Configs & payloads
├── docs/          # Docs & screenshots
├── utils/         # Helper utilities
├── run/           # Execution helpers
├── logs/          # Runtime logs
├── appsec_runner.py
└── requirements.txt

🚀 How to Run
pip install -r requirements.txt
python appsec_runner.py


Example target (authorized test app):

http://testphp.vulnweb.com

🚀 How to Run
pip install -r requirements.txt
python appsec_runner.py


Example target (authorized test app):

http://testphp.vulnweb.com
