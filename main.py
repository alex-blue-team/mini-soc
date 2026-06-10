"""
Mini SIEM - Main Entry Point

This file controls the application workflow:
- parses command-line arguments
- selects operating mode
- processes log data
- generates alerts and summaries
"""

import json

from cli import parse_arguments
from parser import read_logs
from correlator import process_event
from correlator import process_events
from reporter import create_summary
from alert import create_alert


def main():

    # Parse and validate command-line arguments
    parse_result = parse_arguments()

    if parse_result is None:
        return

    file_path, mode = parse_result

    # Configure application mode
    if mode == "--streaming":
        STREAMING_MODE = True
        FINAL_SUMMARY_MODE = False

    elif mode == "--summary":
        STREAMING_MODE = False
        FINAL_SUMMARY_MODE = True

    elif mode == "--both":
        STREAMING_MODE = True
        FINAL_SUMMARY_MODE = True

    # Real-time event processing
    if STREAMING_MODE:

        print("\n--- Potential threats in streaming mode ---\n")

        for line in read_logs(file_path):

            result = process_event(line)

            if result:
                create_alert(json.dumps(result, indent=4))

    # Full log analysis and final report
    if FINAL_SUMMARY_MODE:

        print("\n--- Final alert on potential threats ---\n")

        lines = read_logs(file_path)

        summary_failed_logins = process_events(lines)

        result_events = create_summary(summary_failed_logins)

        for result in result_events:
            create_alert(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()