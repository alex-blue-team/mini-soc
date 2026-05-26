# Mini-SIEM Project

A simple Python-based mini-SIEM project for detecting suspicious login activity in Linux log files.

The project analyzes authentication logs, searches for repeated failed login attempts, correlates events by IP address, and generates alerts in JSON format.

---

## Features

- Detects repeated failed login attempts
- Correlates events by IP address
- Generates alerts in JSON format
- User selects log file manually from terminal
- Handles incorrect command usage
- Handles missing/nonexistent files
- Processes multiple test log files
- Supports detection from multiple attacking IP addresses

---

## Project Structure

```text
mini_siem/
│
├── main.py
├── parser.py
├── correlator.py
├── alert.py
│
├── logs/
│   ├── test_01.log
│   ├── test_02.log
│   ├── test_03.log
│   └── test_04.log
│
└── README.md```

## How It Works

1. User starts the program from terminal
2. User provides path to a log file
3. Program reads logs line by line
4. Failed login attempts are extracted
5. Events are correlated by IP address
6. Alert is generated when threshold is reached

---

## Example Usage

Run the program:

```bash
python3 main.py logs/test_01.log
```

If file path is missing:

```bash
Usage: python3 main.py path_file_log
```

If file does not exist:

```bash
File not found
```


### Example Alert
{
    "alert": "Possible brute-force attack detected",
    "ip_address": "192.168.1.10",
    "failed_attempts": 5
}

## Test Logs

The project includes several test log files:

test_01.log — small number of failed logins
test_02.log — larger number of failed logins
test_03.log — heavy brute-force simulation
test_04.log — brute-force activity from two different IP addresses

### Example:

one IP performs 5 failed attempts
second IP performs 20 failed attempts

##Technologies Used

Python 3
JSON
Linux terminal
Log analysis
Event correlation
Video Demonstration

## This short demo shows:

processing different log sizes
brute-force detection
JSON alert generation
incorrect command handling
nonexistent file handling
multi-IP brute-force detection

## Direct link:

https://youtu.be/gYIt7p-wplQ?si=WpMjJW5Rwh6TYRgX

## Future Improvements
Real-time log monitoring
Detection rules configuration
Email or Telegram alerts
Support for additional log formats
Simple dashboard/web interface

#Author

Cybersecurity student building practical blue-team and detection engineering skills through hands-on projects.
