# Coordinates log processing workflows.
# Runs streaming analysis and summary analysis modes.

import json

from cli import get_file_path
from parser import read_logs
from correlator import process_event
from correlator import process_events
from reporter import create_summary
from alert import create_alert


def start_streaming_mode():
	# Process log events one by one and generate alerts immediately.

	print("\n--- Streaming verification result ---\n")
	file_path = get_file_path()

	for line in read_logs(file_path):

		result = process_event(line)

		if result:

			create_alert(json.dumps(result, indent=4))


def start_summary_mode():
	# Analyze the entire log file and generate a final summary.

	print("\n--- Final check result ---\n")

	file_path = get_file_path()
	lines = read_logs(file_path)

	summary_failed_logins = process_events(lines)

	results = create_summary(summary_failed_logins)

	for result in results:

		create_alert(json.dumps(result, indent=4))
