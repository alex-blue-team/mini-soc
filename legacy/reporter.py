"""
reporter.py

Builds final summary report from failed login statistics.
"""

import config


def create_summary(failed_logins):
    """Create structured report from brute-force detection data."""

    results = []

    for ip, count in failed_logins.items():

        # Determine severity level based on thresholds
        if count >= config.CRITICAL_THRESHOLD:
            severity = "Critical"
        elif count >= config.HIGH_THRESHOLD:
            severity = "High"
        elif count >= config.MEDIUM_THRESHOLD:
            severity = "Medium"
        else:
            severity = "Low"

        results.append(
            {
                "event": "brute-force",
                "source": ip,
                "failed_logins": count,
                "severity": severity,
            }
        )

    return results