# Application entry point and workflow orchestrator.
# Coordinates log ingestion, event correlation, report generation and alerting.

import sys
import os

import json

from parser import read_logs
from correlator import process_events
from reporter import create_summary
from alert import create_alert


def main():

	# Validate command-line arguments.
	if len(sys.argv) < 2:
		print("\nUsage: python3 main.py path_log_file\n")
		return

	file_path = sys.argv[1]

	# Verify that the specified log file exists.
	if not os.path.exists(file_path):
		print("\nFile not found\n")
		return

	# Read log entries from the source file.
	lines = read_logs(file_path)

	# Correlate failed login events by source IP.
	failed_logins = process_events(lines)

	# Generate security findings and severity ratings.
	results = create_summary(failed_logins)

	# Display generated alerts.
	for result in results:
		create_alert(json.dumps(result, indent=4))


if __name__ == "__main__":
	main()