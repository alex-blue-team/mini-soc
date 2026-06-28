"""
correlator.py

Detects brute-force login attempts based on failed logins per IP.
"""

import re
import config


class BruteForceDetector:
    """Tracks failed login attempts and generates security alerts."""

    def __init__(self):
        # Stores number of failed logins per IP
        self.failed_logins = {}

    def process_event(self, line):

        ip = _extract_failed_login_ip(line)

        if ip is None:
            return

        # Increase counter for this IP
        self.failed_logins[ip] = self.failed_logins.get(ip, 0) + 1

        count = self.failed_logins[ip]
        severity = None

        # Determine alert severity
        if count == config.CRITICAL_THRESHOLD:
            severity = "Critical"
        elif count == config.HIGH_THRESHOLD:
            severity = "High"
        elif count == config.MEDIUM_THRESHOLD:
            severity = "Medium"

        if severity:
            return {
                "event": "brute-force",
                "source": ip,
                "failed_logins": count,
                "severity": severity,
            }

    def process_events(self, lines):
        """Process batch of log lines."""

        for line in lines:

            ip = _extract_failed_login_ip(line)

            if ip is None:
                continue

            self.failed_logins[ip] = self.failed_logins.get(ip, 0) + 1

        return self.failed_logins


def _extract_failed_login_ip(line):

    if "failed login" not in line.lower():
        return None

    ip = _extract_ip(line)

    if ip == "unknown":
        return None

    return ip


def _extract_ip(line):

    # Extract IPv4 address from log line
    match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)

    if match:
        return match.group()

    return "unknown"
