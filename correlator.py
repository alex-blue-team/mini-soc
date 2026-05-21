import re

# Stores failed login attempts by IP
failed_logins = {}


def count_events(line):

    # Detect failed login attempts
    if "failed login" in line.lower():

        ip = extract_ip(line)

        if ip == "unknown":
            return None

        # Count attempts for each IP
        if ip not in failed_logins:
            failed_logins[ip] = 0

        failed_logins[ip] += 1

        severity = None

        # Define threat severity levels
        if failed_logins[ip] == 5:
            severity = "Low"

        elif failed_logins[ip] == 20:
            severity = "Medium"

        elif failed_logins[ip] == 100:
            severity = "Critical"

        # Return alert data as JSON-ready dictionary
        if severity:
            return {
                "event": "brute-force",
                "source": ip,
                "failed login": failed_logins[ip],
                "severity": severity,
            }

    return None


def extract_ip(line):

    # Extract IPv4 address from log line
    match = re.search(r"\d+\.\d+\.\d+\.\d+", line)

    if match:
        return match.group()

    return "unknown"