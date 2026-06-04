# reporter.py responsible for:
# - Processing aggregated correlation results
# - Assigning final severity levels
# - Building structured summary reports for analysis output


def create_summary(summary_failed_logins):
    """
    Final summary report generator.

    Converts aggregated failed login statistics into
    structured security events with severity classification.
    """

    results = []

    for ip in summary_failed_logins:

        count_failures = summary_failed_logins[ip]

        # Final severity classification based on total failed attempts
        if count_failures >= 100:
            severity = "Critical"

        elif count_failures >= 20:
            severity = "High"

        elif count_failures >= 5:
            severity = "Medium"

        else:
            severity = "Low"

        # Build structured event for output layer
        results.append({
            "event": "brute-force",
            "source": ip,
            "failed_logins": count_failures,
            "severity": severity
        })

    return results
