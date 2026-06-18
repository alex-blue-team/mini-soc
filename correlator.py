# Correlates log events and detects brute-force activity.
# Tracks failed login attempts and assigns severity levels.

import re


# Detection thresholds.
CRITICAL_THRESHOLD = 100
HIGH_THRESHOLD = 20
MEDIUM_THRESHOLD = 5


# Stores failed login counters by source IP.
failed_logins = {}


def process_event(line):
	# Process a single log entry in streaming mode.

	if "failed login" in line.lower():

		ip = extract_ip(line)

		if ip == "unknown":
			return None

		failed_logins[ip] = failed_logins.get(ip, 0) + 1

		count = failed_logins[ip]

		severity = None

		if count == CRITICAL_THRESHOLD:
			severity = "Critical"

		elif count == HIGH_THRESHOLD:
			severity = "High"

		elif count == MEDIUM_THRESHOLD:
			severity = "Medium"

		if severity:
			return {
				"event": "brute-force",
				"source": ip,
				"failed login": count,
				"severity": severity
				}


def process_events(lines):
	# Aggregate failed login events for summary reporting.

	summary_failed_logins = {}

	for line in lines:

		if "failed login" in line.lower():

			ip = extract_ip(line)

			if ip == "unknown":
				continue

			summary_failed_logins[ip] = summary_failed_logins.get(ip, 0) + 1

	return summary_failed_logins


def extract_ip(line):
	# Extract an IPv4 address from a log entry.

	match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)

	if match:
		return match.group()

	return "unknown"