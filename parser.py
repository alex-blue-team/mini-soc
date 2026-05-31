# Log ingestion module.
# Reads log entries from a file and provides them as a stream for processing.

def read_logs(file_path):

	# Open the log file in read-only mode.
	with open(file_path, "r", encoding="utf-8", errors="ignore") as f:

		# Yield log entries one by one instead of loading the entire file into memory.
		for line in f:
			yield line.strip()
