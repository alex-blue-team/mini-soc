'
# mini-soc

Simple educational Mini-SOC project for log analysis.

## Description

This project simulates a basic SOC (Security Operations Center) pipeline.

It reads log files line by line using a generator and analyzes them for suspicious activity using a simple keyword-based detection module.

## Features

- Stream-based log reading (generator)
- Keyword-based detection (error, failed, invalid)
- Real-time alert output

## Project Structure

- parser.py — reads log files line by line
- detector.py — detects suspicious patterns in log lines
- test_parser.py — main script (pipeline controller)
- test.log — sample log file

## How It Works

log file → parser → detector → alert output

1. The parser reads the log file line by line
2. Each line is passed to the detector
3. The detector checks for suspicious keywords
4. Alerts are printed if a match is found

## Usage

Run the main script:

python test_parser.py

## Example Output

Normal log line
[ALERT] Failed login attempt
Another normal line
[ALERT] error detected in system

## Future Improvements

- Return matched keywords instead of True/False
- Add alert statistics (counting events)
- Save alerts to a separate file
- Add timestamp parsing


## About Me

I am a beginner cybersecurity specialist focusing on SOC analysis and log investigation.

This project is part of my hands-on learning journey, where I build tools from scratch to better understand how log parsing, detection, and alerting work in real environments.

My goal is to become a Junior SOC Analyst and work remotely, with a long-term plan to relocate to Spain.

I am actively learning Python, networking, and security fundamentals, and continuously improving my practical skills through small but real projects like this one.
