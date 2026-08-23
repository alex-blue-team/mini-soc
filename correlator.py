import re
from datetime import datetime

import config


class BruteForceDetector:

    def __init__(self):
        self.failed_login_timestamps = {}

    def process_event(self, log_line):

        source_ip = _extract_failed_login_ip(log_line)

        if not source_ip:
            return None

        timestamp_string = _extract_timestamp(log_line)
        event_timestamp = datetime.fromisoformat(timestamp_string)

        if source_ip not in self.failed_login_timestamps:
            self.failed_login_timestamps[source_ip] = []

        self.failed_login_timestamps[source_ip].append(event_timestamp)

        active_timestamps = _remove_old_timestamps(
            self.failed_login_timestamps[source_ip],
            event_timestamp
        )

        self.failed_login_timestamps[source_ip] = active_timestamps

        failed_login_count = len(active_timestamps)

        severity = _determine_severity(failed_login_count)

        if severity:
            return {
                "event": "brute-force",
                "source": source_ip,
                "failed logins": failed_login_count,
                "port": 45223,
                "severity": severity
            }

        return None

    def process_events(self, log_lines):

        alerts = []

        for log_line in log_lines:

            alert = self.process_event(log_line)

            if alert:
                alerts.append(alert)

        return alerts


def _extract_failed_login_ip(log_line):

    if "failed login" not in log_line:
        return None

    source_ip = _extract_ip(log_line)

    if source_ip == "unknown":
        return None

    return source_ip


def _extract_ip(log_line):

    ip_match = re.search(
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        log_line
    )

    if ip_match:
        return ip_match.group()

    return "unknown"


def _extract_timestamp(log_line):

    log_parts = log_line.split()

    return log_parts[0]


def _remove_old_timestamps(timestamps, current_timestamp):

    active_timestamps = []

    for event_timestamp in timestamps:

        time_difference = (
            current_timestamp - event_timestamp
        )

        difference_seconds = time_difference.total_seconds()

        if difference_seconds <= config.TIME_WINDOW_SECONDS:
            active_timestamps.append(event_timestamp)

    return active_timestamps


def _determine_severity(failed_login_count):

    if failed_login_count == config.MEDIUM_THRESHOLD:
        return "Medium"

    if failed_login_count == config.HIGH_THRESHOLD:
        return "High"

    if failed_login_count == config.CRITICAL_THRESHOLD:
        return "Critical"

    return None