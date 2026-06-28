"""
runner.py

Controls execution flow of the mini-SIEM system.
Starts streaming or summary processing modes.
"""

import json

from correlator import BruteForceDetector
from cli import take_file_path
from parser import read_logs
from reporter import create_summary
from alert import create_alert


def start_streaming_mode():
    """Real-time processing of log lines."""

    print("\n--- Streaming mode check result ---\n")

    file_path = take_file_path()
    detector = BruteForceDetector()

    for line in read_logs(file_path):

        result = detector.process_event(line)

        if result:
            create_alert(json.dumps(result, indent=4))


def start_summary_mode():
    """Batch processing of log file."""

    print("\n--- Check result in final mode ---\n")

    file_path = take_file_path()
    lines = read_logs(file_path)

    detector = BruteForceDetector()

    failed_logins = detector.process_events(lines)
    results = create_summary(failed_logins)

    for result in results:
        create_alert(json.dumps(result, indent=4))