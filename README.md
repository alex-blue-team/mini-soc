# Mini SIEM v7

A lightweight Python-based SIEM-inspired log analysis tool designed for learning cybersecurity, log correlation, and event detection concepts.

The project analyzes log files, detects brute-force login activity, and generates alerts based on configurable severity thresholds.

---

## Overview

This project simulates a simplified Security Information and Event Management (SIEM) workflow.

The application processes log files, detects repeated failed login attempts, correlates events by source IP address, and generates alerts according to predefined severity levels.

Two independent operating modes are available:

- Streaming Mode
- Final Summary Mode

These modes can be enabled separately or simultaneously through the configuration file.

---

## Features

- Streaming event detection
- Final summary reporting
- Brute-force attack detection
- Severity classification (Medium, High, Critical)
- Modular architecture
- Generator-based log processing
- Configurable execution modes

---

## Technologies Used

- Python 3
- Regular Expressions (`re`)
- JSON output (`json`)
- Generators (`yield`)
- Dictionaries for event correlation
- Modular project structure
- Command-line interface (CLI)

---

## Detection Logic

The system monitors log entries for failed login attempts and correlates events by source IP address.

Severity levels:

- 5 failed logins → Medium
- 20 failed logins → High
- 100 failed logins → Critical

---

## Operating Modes

The application supports two independent operating modes which can be enabled separately or simultaneously in `config.py`.

### 1. Streaming Mode

Processes log entries one by one and immediately generates alerts when detection thresholds are reached.

Benefits:

- Real-time style processing
- Immediate alert generation
- Demonstrates event correlation logic

### 2. Final Summary Mode

Processes the entire log file first and then generates a consolidated summary report for all detected source IP addresses.

Benefits:

- Complete overview of detected activity
- Useful for historical log analysis
- Demonstrates reporting and aggregation logic

---

## Architecture

### Streaming Mode

```text
Log File -> Parser -> Correlator -> Alert
```

### Final Summary Mode

```text
Log File -> Parser -> Correlator -> Reporter -> Alert
```

---

## Project Structure

```text
mini-siem-v7/

├── main.py
├── parser.py
├── correlator.py
├── reporter.py
├── alert.py
├── config.py
└── logs/
```

---

## Example Usage

Run the application:

```bash
python3 main.py path_to_log_file
```

Example:

```bash
python3 main.py test_04.log
```

---

## Example Alert

```json
{
    "event": "brute-force",
    "source": "185.234.217.45",
    "failed_logins": 23,
    "severity": "High"
}
```

---

## Demo Video

Project demonstration:

https://youtu.be/c6k_YJ6tBGM?si=wWARJs6_ffhi72rd
---

## Learning Goals

This project was built to practice:

- Log parsing
- Event correlation
- Detection engineering concepts
- SIEM-style workflows
- Python programming
- Modular software design

---

## Author

An aspiring cybersecurity professional passionate about computer science, security engineering, and continuous learning.

Currently building hands-on projects in Python and cybersecurity while working toward a professional career in Spain.
