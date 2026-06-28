# Mini SIEM v8.2

A lightweight Python-based SIEM-inspired log analysis tool designed for learning cybersecurity, log correlation, detection engineering, and event-driven architecture concepts.

This version evolves v8.1 into a more structured object-oriented architecture with improved separation of responsibilities and a dedicated detection engine.

---

## Overview

This project simulates a simplified Security Information and Event Management (SIEM) workflow.

The system processes log files, detects brute-force login activity, correlates events by source IP address, and generates alerts based on predefined severity thresholds.

In v8.2, the system is refactored into a fully modular pipeline with a clear execution controller and dedicated correlation engine.

---

## Key Improvements in v8.2

- Introduced object-oriented correlation engine (`correlator.py`)
- Separated execution logic into `runner.py`
- Clear CLI isolation in `cli.py`
- Centralized configuration in `config.py`
- Improved parser isolation for log ingestion
- Dedicated alert system module
- Cleaner reporting layer (`reporter.py`)
- Better scalability for future detection rules
- Foundation prepared for time-window and advanced correlation logic

---

## Features

- Streaming event detection (real-time processing)
- Final summary reporting (batch analysis)
- Combined dual-mode execution
- Full CLI-based control
- Input validation and error handling
- Detection of invalid file paths and arguments
- Modular architecture (OOP-based core engine)
- Generator-based log processing
- Dedicated execution orchestration layer
- Configurable severity thresholds
- Extensible correlation engine

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

## Architecture (v8.2)

```
mini-siem-v8.2/

├── main.py                 # Entry point
├── cli.py                  # CLI argument parsing
├── runner.py              # Execution controller (modes)
├── correlator.py          # Brute-force detection engine (OOP)
├── reporter.py            # Summary generation
├── parser.py              # Log file reader
├── alert.py               # Alert output system
├── config.py              # Central configuration
│
├── test_log/              # Sample log datasets
├── legacy/                # Previous implementations (archived)
│
├── V8_SPEC.md             # Technical specification
├── README.md              # Documentation
└── .gitignore             # Ignored files configuration
```

---

## Core Execution Flow

### Streaming Mode

```text
Log File
    ↓
CLI
    ↓
Runner
    ↓
Parser
    ↓
Alert Engine
```

### Summary Mode

```text
Log File
    ↓
CLI
    ↓
Runner
    ↓
Parser
    ↓
Correlator (OOP Engine)
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
Streaming Pipeline + Correlation Engine
    ↓
Alerts + Report
```

---

## Core Modules

### main.py
Entry point of the system. Initializes CLI and launches execution pipeline.

### cli.py
Parses command-line arguments and validates runtime options.

### runner.py
Controls execution modes (streaming, summary, both) and orchestrates system flow.

### parser.py
Reads and normalizes raw log files into structured events.

### correlator.py
Object-oriented brute-force detection engine.
Implements correlation logic across events grouped by source IP.

### alert.py
Handles alert generation and formatting.

### reporter.py
Generates aggregated summary reports based on correlated events.

### config.py
Central configuration for thresholds, rules, and system parameters.

---

## Detection Logic

The system detects brute-force login activity using configurable thresholds:

```python
CRITICAL_THRESHOLD = 100
HIGH_THRESHOLD = 20
MEDIUM_THRESHOLD = 5
```

Severity is assigned based on the number of failed login attempts per source IP.

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

## Operating Modes

### 1. Streaming Mode

Processes log entries one by one and generates alerts in real time.

### 2. Summary Mode

Processes full log file and generates aggregated detection report.

### 3. Both Mode

Combines streaming + summary analysis for full visibility.

---

## Test Data

Directory `test_log/` contains sample datasets for testing detection logic and validating system behavior.

---

## Legacy Code

Directory `legacy/` stores previous implementations for reference and backward compatibility.

---

## Version 8.2 Changes (Summary)

- Introduced OOP-based correlation engine
- Separated execution controller (`runner.py`)
- Improved modular pipeline design
- Strengthened separation of concerns
- Prepared architecture for advanced detection features
- Improved scalability for future SIEM extensions

---

## Learning Goals

This project was built to practice:

- Log parsing
- Event correlation
- Detection engineering concepts
- SIEM-style workflows
- Object-oriented design
- Modular Python architecture
- CLI application development
- Input validation and error handling
- Software refactoring
- Security monitoring fundamentals

---

## Future Improvements (v8.3 direction)

Planned improvements:

- Time-window based correlation engine
- Rule-based detection system expansion
- Advanced alert scoring model
- Performance optimization for large logs
- Plugin-based detection architecture

---

## Author

An aspiring cybersecurity engineer focused on SOC operations, detection engineering, and security automation.

Currently building structured SIEM-like systems in Python as part of a long-term learning path toward professional cybersecurity roles in Europe.