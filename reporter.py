# Generates summary reports from correlated log events.
# Assigns severity levels based on failed login counts.


# Detection thresholds.
CRITICAL_THRESHOLD = 100
HIGH_THRESHOLD = 20
MEDIUM_THRESHOLD = 5


def create_summary(summary_failed_logins):
	# Create a summarized report for each source IP.

	results = []

	for ip in summary_failed_logins:

		count = summary_failed_logins[ip]

		if count >= CRITICAL_THRESHOLD:
			severity = "Critical"

		elif count >= HIGH_THRESHOLD:
			severity = "High"

		elif count >= MEDIUM_THRESHOLD:
			severity = "Medium"

		else:
			severity = "Low"

		results.append({
				"event": "brute-force",
				"source": ip,
				"failed login": count,
				"severity": severity
				}
				)

	return results