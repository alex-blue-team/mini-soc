# Mini SIEM v9.0

A lightweight Python-based SIEM-inspired log analysis tool designed for learning cybersecurity, log analysis, event correlation, detection engineering, and security automation concepts.

Version 9.0 introduces the first working implementation of time-window-based event correlation, allowing the system to detect brute-force login activity based not only on the number of failed login attempts, but also on how many attempts occur within a defined period of time.

This project is an educational and continuously evolving implementation of a simplified SIEM-style detection pipeline.

---

## Overview

This project simulates a simplified Security Information and Event Management (SIEM) workflow.

The system reads log files, identifies failed login events, extracts source IP addresses and timestamps, correlates events belonging to the same source, and generates alerts when the number of failed login attempts reaches predefined severity thresholds within a configured time window.

The main architectural change introduced in v9.0 is the transition from simple event counting to time-window-based correlation.

Instead of only asking:

> How many failed login attempts came from this IP?

the system now asks:

> How many failed login attempts came from this IP within the defined time window?

This provides a more realistic foundation for security event correlation and future detection engineering work.

---

## Key Improvements in v9.0

- Introduced time-window-based correlation
- Replaced simple failed-login counters with timestamp tracking
- Added timestamp extraction from log entries
- Added conversion of timestamps to Python `datetime` objects
- Added removal of timestamps outside the active time window
- Added sliding-window event counting
- Updated brute-force detection thresholds
- Improved separation of CLI, parsing, correlation, execution, and alert output
- Continued use of an object-oriented detection engine
- Preserved streaming and summary processing modes
- Prepared the project for future multi-language and API integration

---

## Features

- Streaming event detection
- Summary/batch analysis
- Combined dual-mode execution
- Time-window-based brute-force detection
- Sliding time-window correlation
- Correlation of failed login events by source IP
- Timestamp extraction and processing
- Configurable time window
- Configurable severity thresholds
- Full CLI-based control
- Input validation and error handling
- Detection of invalid file paths and arguments
- Modular Python architecture
- Object-oriented detection engine
- Generator-based log processing
- Dedicated execution orchestration layer
- JSON-formatted alerts
- Archived legacy implementations

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

### Examples

Streaming mode:

```bash
python3 main.py test.log --streaming
```

Summary mode:

```bash
python3 main.py test.log --summary
```

Combined mode:

```bash
python3 main.py test.log --both
```

---

## Input Validation

The system validates command-line input before starting log processing.

The CLI checks:

- Number of supplied arguments
- Log file existence
- Selected operating mode
- Excess arguments
- Invalid operating modes

Examples of invalid input include:

```bash
python3 main.py
```

```bash
python3 main.py test.log
```

```bash
python3 main.py test.log --streaming extra
```

```bash
python3 main.py test.log --invalid
```

The application provides guidance when incorrect input is detected.

---

## Architecture (v9.0)

```text
mini-siem-v9.0/

├── main.py                 # Application entry point
├── cli.py                  # CLI argument validation
├── runner.py               # Execution controller
├── correlator.py           # Brute-force detection and Time Window
├── parser.py               # Log file reader
├── alert.py                # Alert output
├── config.py               # Central configuration
│
├── test_log/               # Sample log datasets
├── legacy/                 # Previous implementations (archived)
│
├── README.md               # Documentation
└── .gitignore              # Git ignore configuration
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
BruteForceDetector
    ↓
Time Window
    ↓
Correlation
    ↓
Alert
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
BruteForceDetector
    ↓
Time Window
    ↓
Correlation
    ↓
Collected Alerts
```

### Combined Mode

```text
Log File
    ↓
CLI
    ↓
Runner
    ↓
Parser
    ↓
Detection Engine
    ↓
Streaming + Summary Processing
    ↓
Alerts
```

---

## Core Modules

### main.py

Entry point of the system.

The main function:

- validates command-line input;
- determines the selected operating mode;
- starts the corresponding execution process.

### cli.py

Handles command-line input and validation.

It checks:

- required arguments;
- file path;
- number of arguments;
- selected operating mode.

### runner.py

Controls the execution flow for the selected mode.

It connects the parser, detection engine, and alert output.

### parser.py

Reads the log file using a Python generator.

Each log line is returned individually after basic normalization.

This allows the system to process log entries sequentially rather than loading the complete file into memory.

### correlator.py

Contains the main detection engine.

The `BruteForceDetector` class:

- identifies failed login events;
- extracts source IP addresses;
- extracts timestamps;
- converts timestamps into Python `datetime` objects;
- stores timestamps by source IP;
- removes timestamps outside the active Time Window;
- counts active failed login events;
- determines severity;
- generates detection results.

### alert.py

Handles alert output.

The current implementation keeps the alert layer intentionally simple and prints generated alerts to the terminal.

### config.py

Contains central configuration values used by the application.

---

## Time Window

The main new feature in v9.0 is the Time Window.

The current configuration is:

```python
TIME_WINDOW_SECONDS = 60
```

This means that the detector considers failed login events occurring within a 60-second period.

In previous versions, failed login activity was represented mainly as a simple counter:

```text
IP → number of failed logins
```

In v9.0, the system stores timestamps:

```text
IP → [timestamp1, timestamp2, timestamp3, ...]
```

For example:

```text
10.10.10.5 →
    12:00:05
    12:00:12
    12:00:24
    12:00:41
```

When a new event arrives, the detector evaluates the timestamps and removes events that are outside the active Time Window.

The remaining timestamps represent the currently relevant events.

---

## Time Window Processing

The current processing sequence is:

```text
New Log Event
      ↓
Extract Source IP
      ↓
Extract Timestamp
      ↓
Convert Timestamp to datetime
      ↓
Store Timestamp
      ↓
Remove Old Timestamps
      ↓
Count Active Events
      ↓
Determine Severity
      ↓
Generate Alert
```

This creates the first working sliding-window correlation mechanism in the project.

---

## Detection Logic

The current severity thresholds are:

```python
MEDIUM_THRESHOLD = 4
HIGH_THRESHOLD = 6
CRITICAL_THRESHOLD = 9
```

The detector evaluates the number of failed login events currently inside the Time Window.

Conceptually:

```text
Less than 4
    ↓
No alert

4
    ↓
Medium

6
    ↓
High

9
    ↓
Critical
```

The detection therefore depends on four elements:

```text
Source IP
    +
Failed Login Events
    +
Time Window
    +
Severity Threshold
```

---

## Example Detection Scenario

Assume the configured Time Window is 60 seconds.

A source IP generates these failed login events:

```text
12:00:05
12:00:12
12:00:24
12:00:41
12:00:57
```

At `12:00:57`, five failed login events are currently inside the active window.

Therefore:

```text
Failed logins: 5
Time window: 60 seconds
Severity: Medium
```

If older events move outside the active Time Window, they are removed from the correlation data and no longer contribute to the current event count.

This is the main difference between simple event counting and time-window-based correlation.

---

## Example Alert

A generated alert has the following structure:

```json
{
    "event": "brute-force",
    "source": "185.234.217.45",
    "failed logins": 6,
    "port": 45223,
    "severity": "High"
}
```

The alert represents brute-force activity associated with a source IP whose failed login activity reached the configured threshold within the active Time Window.

---

## Operating Modes

### 1. Streaming Mode

Processes log entries sequentially.

Each event is passed to the detection engine immediately.

This mode is intended to simulate event-by-event security monitoring.

### 2. Summary Mode

Processes the complete log file and collects generated alerts.

This mode is useful for analysing an existing log dataset.

### 3. Both Mode

Runs both available processing modes.

This allows the project to demonstrate both event-by-event processing and final collected results.

---

## Test Data

The `test_log/` directory contains sample log datasets used for testing the detection engine.

Test data is used to validate:

- timestamp extraction;
- timestamp conversion;
- failed login detection;
- source IP extraction;
- Time Window behaviour;
- event correlation;
- threshold detection;
- alert generation.

The test datasets are part of the learning process and may evolve as the project develops.

---

## Legacy Code

The `legacy/` directory stores selected components from previous versions of the project.

These files are no longer part of the active v9.0 execution pipeline.

They are preserved to document the development and refactoring process.

The directory currently contains previous implementations such as:

```text
legacy/
├── config.py
├── correlator.py
└── reporter.py
```

These files are not required to run v9.0.

The legacy directory is maintained as an archive rather than as part of the current application architecture.

---

## Project Evolution

The project has evolved through several stages:

```text
Basic Log Processing
        ↓
Failed Login Counting
        ↓
Brute-Force Correlation
        ↓
Object-Oriented Detection Engine
        ↓
Modular Architecture
        ↓
Time-Window Correlation
```

Version 9.0 represents an important step because the detection engine now considers not only the number of security events, but also their temporal relationship.

---

## Why Time Windows Matter

A simple counter can answer:

> How many failed login attempts came from this IP?

A Time Window can answer:

> How many failed login attempts came from this IP within a defined period?

These are very different security questions.

For example:

```text
10 failed logins
over several hours
```

is different from:

```text
10 failed logins
within 60 seconds
```

Time-based correlation provides a foundation for detecting patterns such as:

- brute-force attacks;
- authentication bursts;
- repeated connection attempts;
- suspicious event frequency;
- other time-dependent security behaviours.

The current implementation focuses on brute-force authentication activity as the first practical use case.

---

## Learning Goals

This project was built to practice:

- Python programming
- Linux log analysis
- Log parsing
- Timestamp processing
- Python `datetime`
- Event correlation
- Time-window correlation
- Detection engineering concepts
- Brute-force detection
- Severity classification
- SIEM-style workflows
- Object-oriented programming
- Modular Python architecture
- CLI application development
- Input validation
- Generators
- Refactoring
- Security monitoring fundamentals

The project is intentionally developed step by step instead of attempting to reproduce the complexity of a production SIEM from the beginning.

---

## Current Limitations

This project is an educational implementation and should not be considered a production SIEM.

Current limitations include:

- Limited log format support
- IPv4-focused detection
- Simplified timestamp extraction
- Simplified IP address extraction
- A single primary detection rule
- Basic alert formatting
- Local file-based log ingestion
- No database
- No persistent event storage
- No web interface
- No authentication system
- No distributed processing
- No production-scale deployment architecture

These limitations are intentional at the current stage of development.

The goal is to understand the underlying concepts before introducing additional system complexity.

---

## Future Improvements

The next major development stage is planned as v9.1.

Potential improvements include:

- Stronger timestamp validation
- Improved handling of malformed log entries
- Improved IP address validation
- Cleaner Time Window abstraction
- More explicit separation between detection and alert generation
- Improved severity threshold logic
- Richer alert information
- Expanded test scenarios
- Further architectural refinement
- Additional detection rules

After v9.1, the project is planned to explore interaction between Python and Go.

The first planned multi-language architecture will be intentionally minimal:

```text
Python Mini-SIEM
        ↓
      JSON
        ↓
   Go Analyzer
```

A later stage will introduce basic API interaction:

```text
Python
   ↓
 HTTP / JSON
   ↓
 API
   ↓
 Go
```

These components are future development goals and are not part of v9.0.

---

## Project Philosophy

The project is being developed incrementally.

Each version introduces a practical concept, implements it, tests it, and then uses the result as a foundation for the next stage.

The general development process is:

```text
Understand
    ↓
Implement
    ↓
Test
    ↓
Find Problems
    ↓
Refactor
    ↓
Understand More Deeply
    ↓
Build the Next Version
```

The purpose is not simply to produce a large amount of code.

The purpose is to understand how security monitoring systems work by building their individual components step by step.

---

## Author

An aspiring cybersecurity engineer focused on SOC operations, detection engineering, security monitoring, and security automation.

This project is part of a long-term hands-on learning journey focused on understanding cybersecurity through practical implementation.

---

## Disclaimer

This project is intended for educational and research purposes.

It is a personal learning project designed to explore SIEM concepts, log analysis, event correlation, detection engineering, Python programming, and security automation.

It is not intended to replace a production SIEM or to be used as a production security monitoring system.