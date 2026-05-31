# Correlation engine.
# Detects failed login events and aggregates them by source IP address.

import re


failed_logins = {}

def process_events(lines):

	# Process log entries and count failed logins per IP address.
	for line in lines:

		if "failed login" in line.lower():
		
			ip = extract_ip(line)

			# Skip events where no valid IP address was found.
			if ip == "unknown":
				continue

			# Create a counter for a new IP address.
			if ip not in failed_logins:
				failed_logins[ip] = 0

			# Increment the failed login counter.
			failed_logins[ip] += 1

	return failed_logins


def extract_ip(line):

	# Extract an IPv4 address from a log entry.
	match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)

	if match:
		return match.group()

	return "unknown"
