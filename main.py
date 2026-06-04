# main.py Entry point for Mini SIEM v7
#
# This module controls execution flow of the system.
# It coordinates:
# - Log ingestion
# - Streaming detection mode
# - Final summary reporting mode
# - Output formatting and alert generation

import sys
import os
import json

from parser import read_logs
from config import STREAMING_MODE, FINAL_SUMMARY_MODE
from correlator import process_event, process_events
from reporter import create_summary
from alert import create_alert



def main():

    # Validate CLI arguments
    if len(sys.argv) < 2:
        print("\nUsage: python3 main.py path_log_file\n")
        return

    file_path = sys.argv[1]

    # Ensure log file exists before processing
    if not os.path.exists(file_path):
        print("\nFile not found\n")
        return

    # -------------------------------
    # STREAMING MODE (real-time alerts)
    # -------------------------------
    if STREAMING_MODE:

        print("\n--- Streaming Mode: Real-time detection ---\n")

        for line in read_logs(file_path):

            result = process_event(line)

            if result:
                create_alert(json.dumps(result, indent=4))

    # -------------------------------
    # FINAL SUMMARY MODE (batch report)
    # -------------------------------
    if FINAL_SUMMARY_MODE:

        print("\n--- Final Summary Mode: Aggregated report ---\n")

        lines = read_logs(file_path)

        summary_failed_logins = process_events(lines)

        results = create_summary(summary_failed_logins)

        for result in results:
            create_alert(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
