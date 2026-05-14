# Correlation module for detecting suspicious login activity.

import re

# Stores failed login attempts by IP address
failed_logins = {}


def count_events(line):

    # Detect failed login attempts
    if "failed login" in line.lower():

        # Extract IP address from log line
        ip = extract_ip(line)

        # Ignore logs without valid IP
        if ip == "unknown":
            return None

        # Create counter for new IP
        if ip not in failed_logins:
            failed_logins[ip] = 0

        # Increase failed login counter
        failed_logins[ip] += 1

        # Detect possible brute-force attack
        if failed_logins[ip] >= 5:
            return f"Possible brute-force attack from {ip} (failed login: {failed_logins[ip]})"

    return None


def extract_ip(line):

    # Search for IPv4 address in log line
    match = re.search(r"\d+\.\d+\.\d+\.\d+", line)

    if match:
        return match.group()

    return "unknown"
