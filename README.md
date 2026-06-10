# Mini SIEM v8

A lightweight Python-based SIEM-inspired log analysis tool designed for learning cybersecurity, log correlation, and event detection concepts.

This version significantly improves command-line control, modular execution modes, and user input validation, making the tool fully CLI-driven.

---

## Overview

This project simulates a simplified Security Information and Event Management (SIEM) workflow.

The system processes log files, detects brute-force login activity, correlates events by source IP address, and generates alerts based on predefined severity thresholds.

### Key Improvements in v8

- Full CLI-based execution
- Runtime mode selection through terminal arguments
- Input validation and user-friendly error handling
- Removal of configuration-based mode selection

---

## Features

- Streaming event detection (real-time processing)
- Final summary reporting (batch analysis)
- Combined dual-mode execution
- Full CLI-based control
- User input validation and error handling
- Detection of invalid file paths and arguments
- Modular architecture
- Generator-based log processing

---

## Command Line Interface (CLI)

The application is executed using explicit runtime arguments:

```bash
python3 main.py <log_file> <mode>
```

### Available Modes

- `--streaming`
- `--summary`
- `--both`

---

## Input Validation

The system includes robust validation of user input:

- Checks number of arguments
- Validates log file existence
- Validates selected operating mode
- Displays helpful error messages for incorrect usage

---

## Operating Modes

### 1. Streaming Mode

Processes log entries one by one and generates alerts in real time.

**Benefits:**

- Immediate detection
- Simulates live SIEM monitoring
- Fast response to threats

### 2. Summary Mode

Processes the full log file and generates a final aggregated report.

**Benefits:**

- Complete overview of system activity
- Useful for forensic analysis
- Aggregated detection results

### 3. Both Mode

Runs streaming and summary analysis together.

**Benefits:**

- Combines real-time and batch analysis
- More complete security visibility

---

## Architecture

### Streaming Mode

```text
Log File → CLI Parser → Event Processor → Alert System
```

### Summary Mode

```text
Log File → CLI Parser → Correlator → Reporter → Alert System
```

### Combined Mode

```text
Log File → CLI Parser → Streaming Analysis + Summary Analysis → Alerts
```

---

## Project Structure

```text
mini-siem-v8/

├── main.py
├── cli.py
├── parser.py
├── correlator.py
├── reporter.py
├── alert.py
└── legacy/
```

---

## Example Usage

### Streaming Mode

```bash
python3 main.py test_04.log --streaming
```

### Summary Mode

```bash
python3 main.py test_04.log --summary
```

### Combined Mode

```bash
python3 main.py test_04.log --both
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

https://youtu.be/Mip7U6Uhl3I?si=aGYiWxGjQ1goMhaZ

---

## Learning Goals

This project was built to practice:

- Log parsing
- Event correlation
- Detection engineering concepts
- SIEM-style workflows
- Python programming
- Modular software design
- CLI application development
- Input validation and error handling

---

## Future Improvements (v8.1)

Planned improvements for the next version:

- Refactor `main.py` into a cleaner orchestration layer
- Improve separation of execution logic
- Simplify mode management
- Prepare the project for time-window based detection

---

## Author

An aspiring cybersecurity professional passionate about computer science, security engineering, and continuous learning.

Currently building hands-on projects in Python and cybersecurity while working toward a professional career in Spain.