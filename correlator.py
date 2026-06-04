
# correlator.py responsible for:
# - Processing log lines in real-time (streaming mode)
# - Correlating failed login attempts per IP address
# - Generating alerts when severity thresholds are reached
# - Aggregating data for final summary reporting mode

import re


failed_logins = {}


def process_event(line):
    """
    Streaming mode processing.
    Analyzes a single log line and returns an alert
    if a severity threshold is reached.
    """

    if "failed login" in line.lower():

        ip = extract_ip(line)

        if ip == "unknown":
            return None

        if ip not in failed_logins:
            failed_logins[ip] = 0

        failed_logins[ip] += 1

        count_failures = failed_logins[ip]
        severity = None

        # Severity thresholds (streaming detection rules)
        if count_failures == 100:
            severity = "Critical"
        elif count_failures == 20:
            severity = "High"
        elif count_failures == 5:
            severity = "Medium"

        if severity:
            return {
                "event": "brute-force",
                "source": ip,
                "failed login": count_failures,
                "severity": severity
            }


def process_events(lines):
    """
    Batch mode processing (final summary mode).
    Builds aggregated statistics of failed logins per IP.
    """

    summary_failed_logins = {}

    for line in lines:

        if "failed login" in line.lower():

            ip = extract_ip(line)

            if ip == "unknown":
                continue

            if ip not in summary_failed_logins:
                summary_failed_logins[ip] = 0

            summary_failed_logins[ip] += 1

    return summary_failed_logins


def extract_ip(line):
    """
    Extracts IPv4 address from a log line.
    Returns 'unknown' if no IP is found.
    """

    match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)

    if match:
        return match.group()

    return "unknown"
