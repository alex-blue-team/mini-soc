# Mini-SIEM V8 Specification


## Supported Commands

### python3 main.py <logfile> --streaming
### python3 main.py <logfile> --summary
### python3 main.py <logfile> --both


## Rules

### Rule 1
Mode selection is mandatory.

### Rule 2
Only one mode argument is allowed.
Additional arguments are not permitted.

### Rule 3
A log file path is  mandatory.

### Rule 4
The specified log file must exist.

### Rule 5
Only supported modes are allowed:
- --streaming
-  --summary
-  --both

### Rule 6
Future enhancement:

If multiple modes specified
(--streaming and --summary),
the system shall automatically use --both.

This feature is not implemented in V8.


## Error Handling

### Error 1
Mode not specified.

### Error 2
Log file not specified.

### Error 3
Log file not found.

### Error 4
Unknown mode specified.

### Error 5
Too many arguments specified.
