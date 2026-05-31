# Reporting module.
# Generates structured security findings and assigns severity levels.

def create_summary(failed_logins):

	results = []

	# Build a security finding for each source IP.
	for ip in failed_logins:

		counted_failures = failed_logins[ip]

		# Determine the severity based on the number of failed logins.
		if counted_failures >= 100:
			severity = "Critical"

		elif counted_failures >= 20:
			severity = "High"

		elif counted_failures >= 5:
			severity = "Medium"

		else:
			severity = "Low"

		# Create a structured report entry.
		results.append({
				"event": "brute-force",
				"source": ip,
				"failed logins": failed_logins[ip],
				"severity": severity})

	return results
