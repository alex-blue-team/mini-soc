# Mini SIEM v8.1

A lightweight Python-based SIEM-inspired log analysis tool designed for learning cybersecurity, log correlation, and event detection concepts.

This version focuses on internal refactoring, cleaner architecture, improved maintainability, and better separation of responsibilities while preserving all existing functionality.

---

## Overview

This project simulates a simplified Security Information and Event Management (SIEM) workflow.

The system processes log files, detects brute-force login activity, correlates events by source IP address, and generates alerts based on predefined severity thresholds.

### Key Improvements in v8.1

- Refactored execution flow into a dedicated `runner.py` module
- Simplified `main.py` into a lightweight application entry point
- Improved separation of responsibilities between modules
- Introduced configurable severity threshold constants
- Replaced list-based mode storage with immutable tuple constants
- Simplified event counting using dictionary `.get()` method
- Reduced code duplication and improved code readability
- Improved maintainability and project structure

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
- Dedicated execution orchestration layer (`runner.py`)
- Configurable severity thresholds

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
Log File
    ↓
CLI
    ↓
Runner
    ↓
Event Processor
    ↓
Alert System
```

### Summary Mode

```text
Log File
    ↓
CLI
    ↓
Runner
    ↓
Correlator
    ↓
Reporter
    ↓
Alert System
```

### Combined Mode

```text
Log File
    ↓
CLI
    ↓
Runner
    ↓
Streaming Analysis + Summary Analysis
    ↓
Alerts
```

---

## Version 8.1 Changes

This release focuses on code quality, maintainability, and internal refactoring.

### Improvements

- Refactored execution flow into a dedicated `runner.py` module
- Simplified `main.py` to a lightweight application entry point
- Improved separation of responsibilities between modules
- Replaced list-based mode storage with immutable tuple constants
- Introduced named severity threshold constants
- Simplified event counting using dictionary `.get()` method
- Reduced code duplication
- Improved readability and maintainability
- Preserved existing functionality while improving architecture

---

## Project Structure

```text
mini-siem-v8.1/

├── main.py
├── runner.py
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
    "failed login": 23,
    "severity": "High"
}
```

---

## Detection Logic

The system currently detects brute-force login activity using configurable severity thresholds.

```python
CRITICAL_THRESHOLD = 100
HIGH_THRESHOLD = 20
MEDIUM_THRESHOLD = 5
```

Severity is assigned automatically based on the number of failed login attempts detected from a single source IP address.

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
- Refactoring techniques
- Software architecture fundamentals

---

## Future Improvements (v8.2)

The next release will focus on object-oriented design and further refactoring.

Planned improvements:

- Replace global variables with dedicated classes
- Encapsulate correlation state inside objects
- Continue improving separation of responsibilities
- Refactor internal application structure
- Improve maintainability and scalability
- Prepare the codebase for additional detection rules
- Lay the foundation for future time-window based detection
- Apply object-oriented programming principles to the SIEM workflow

---

## Author

An aspiring cybersecurity professional passionate about computer science, security engineering, and continuous learning.

Currently building hands-on projects in Python and cybersecurity while working toward a professional career in Spain.

This project is part of a long-term learning journey focused on SOC operations, detection engineering, SIEM concepts, and security automation.