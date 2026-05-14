# mini-soc

Simple educational Mini-SOC project for log analysis and brute-force detection.

## Description

This project simulates a basic SOC (Security Operations Center) pipeline.

It reads log files line by line, analyzes authentication events, extracts IP addresses, and detects possible brute-force attacks based on repeated failed login attempts.

The project is modular and split into separate components for parsing, correlation, and alert generation.

## Features

- Stream-based log reading using generators
- Failed login detection
- IP address extraction from logs
- Simple event correlation
- Brute-force attack detection
- Real-time alert output
- Modular architecture

## Project Structure

- parser.py — reads log files line by line
- correlator.py — analyzes events and detects suspicious activity
- alert.py — generates alert messages
- main.py — main pipeline controller
- detector.py — older keyword-based detector version
- test.log — sample log file

## How It Works

log file → parser → correlator → alert

1. The parser reads the log file line by line
2. The correlator analyzes authentication events
3. IP addresses are extracted from suspicious logs
4. Failed login attempts are counted per IP
5. Alerts are generated when suspicious thresholds are reached

## Detection Logic

The system currently detects:

- Multiple failed login attempts from the same IP
- Possible brute-force attacks after 5 failed attempts

Example:

```text
[ALERT]: Possible brute-force attack from 10.0.0.1 (failed login: 5)
```

## Usage

Run the project:

```bash
python3 main.py
```

## Future Improvements

- Add timestamp parsing
- Save alerts to a separate file
- Detect multiple attack types
- Add configuration support
- Add real-time log monitoring
- Improve log parsing accuracy
- Add alert severity levels

## About Me

I am a beginner cybersecurity specialist focusing on SOC analysis and log investigation.

This project is part of my hands-on learning journey, where I build small security tools from scratch to better understand how log parsing, event correlation, and alerting work in real environments.

My goal is to become a Junior SOC Analyst and continue developing practical cybersecurity skills through real projects and continuous learning.
