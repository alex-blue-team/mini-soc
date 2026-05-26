"""
Main entry point of the mini-SIEM project.

This file reads log lines from a log file,
sends events to the correlator,
and creates alerts when suspicious activity is detected.
"""

import sys
import os
import json

from parser import read_log
from alert import create_alert
from correlator import process_events


def main():

	# Checking if user provided log file path
	if len(sys.argv) < 2:
		print("\nUsage: python3 main.py path_file_log\n")
		return

	# Getting log file path from command line
	file_path = sys.argv[1]

	# Checking if file exists
	if not os.path.exists(file_path):
		print("\nFile not found\n")
		return

	# Reading log file line by line
	for line in read_log(file_path):

		# Processing events and searching for correlations
		result = process_events(line)

		# Creating alert if suspicious activity detected
		if result:
			create_alert(json.dumps(result, indent=4))


if __name__ == "__main__":
	main()
