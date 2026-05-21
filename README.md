# Mini SIEM System (Python)

A simple educational mini-SIEM project written in Python.

The project analyzes log files, detects failed login attempts from the same IP address, and generates alerts based on suspicious activity.

---

## Current Features

✔ Log parsing  
✔ Regex-based IP extraction  
✔ Failed login detection  
✔ Event correlation by source IP  
✔ Threat severity classification  
✔ JSON formatted alerts  
✔ Streaming alert mode  

---

## How It Works

The system reads log files line by line and searches for failed login attempts.

If multiple failed logins are detected from the same IP address, the system increases the internal event counter and classifies the threat severity level.

Current severity thresholds:

- 5 failed logins → Low
- 20 failed logins → Medium
- 100 failed logins → Critical

Alerts are displayed in JSON format for better readability and future SIEM-style processing.

---

## Example Alert


{
    "event": "brute-force",
    "source": "192.168.1.15",
    "failed login": 20,
    "severity": "Medium"
}


## Test Scenarios

The project currently includes multiple test log samples:

test_01.log → Low severity
test_02.log → Medium severity
test_03.log → Critical severity

Log sample switching is currently performed manually inside main.py.


## Screenshots

Version 3

Located in:

screenshots/01/

Version 4

Located in:

screenshots/02/


## Technologies Used

Python
Regex (re)
JSON
Log parsing
Event correlation
Future Plans


## Next planned update

✔ V5 = Final Summary Mode

Streaming alerts will remain available as a separate operational mode.




