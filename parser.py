def read_logs(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as log_file:

        for log_line in log_file:
            yield log_line.strip()