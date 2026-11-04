# 30-days-python-devops-automation
30 days of Python automation projects for DevOps and SRE
# Day 1: Linux Log Analyzer – Python DevOps Automation

## 1. Project Overview

The Linux Log Analyzer is a Python automation project that reads application log files, identifies log levels, counts errors and warnings, and extracts error messages.

In production environments, SRE and DevOps engineers regularly investigate application logs to identify failures and troubleshoot incidents.

Instead of manually reading thousands of log lines, we use Python to automate the analysis.

## 2. Problem Statement – What Issue Are We Solving?

Imagine a production application is experiencing failures.

The application generates logs containing different messages:

- INFO – Normal application activity.
- WARNING – Something needs attention.
- ERROR – An application failure or unexpected problem.

When a production issue occurs, engineers need to:

1. Read application log files.
2. Identify errors and warnings.
3. Count different log levels.
4. Extract error messages.
5. Understand what is happening in the application.

### Problems with manual log analysis

- Reading large log files takes time.
- Important error messages can be missed.
- Counting errors manually is inefficient.
- Repeated manual investigation increases troubleshooting time.

### Our solution

We developed a Python script that automatically reads the log file, counts log levels, and extracts error messages.

**Real-world DevOps use case:** This is a starting point for automating production log analysis and incident investigation.

## 3. Project Structure

```text
30 Day python/
│
├── Linux Log Analyzer.py
├── application.log
└── README.md
```

| File | Purpose |
|---|---|
| `Linux Log Analyzer.py` | Contains Python automation code |
| `application.log` | Contains sample application logs |
| `README.md` | Explains the project |

## 4. Sample Application Logs

```text
2026-11-01 10:00:01 INFO Server started
2026-11-01 10:01:02 ERROR Database connection failed
2026-11-01 10:02:03 WARNING High memory usage
2026-11-01 10:03:04 ERROR API request failed
2026-11-01 10:04:05 INFO User logged in
2026-11-01 10:05:06 ERROR Database connection failed
2026-11-01 10:06:07 WARNING CPU usage high
2026-11-01 10:07:08 ERROR API request failed
```

## 5. Functions We Developed and Why

### Function 1: `read_logs(file_path)`

**Purpose:** Read the application log file.

Why do we need it?
- Opens the log file.
- Reads all log lines.
- Handles the situation where the file does not exist.
- Returns the log data for further processing.

Important Python concepts:
- `open()`
- `with`
- `readlines()`
- `try-except`
- `return`

### Function 2: `count_log_levels(logs)`

**Purpose:** Count INFO, WARNING, and ERROR messages.

Why do we need it?
- Identifies each log level.
- Counts how many times each level appears.
- Helps engineers understand the volume of errors and warnings.

Expected result:

```python
{
    "INFO": 2,
    "WARNING": 2,
    "ERROR": 4
}
```

Important Python concepts:
- Dictionary
- `for` loop
- Conditional statements
- Dictionary values and updates

### Function 3: `find_errors(logs)`

**Purpose:** Extract only ERROR messages from the log file.

Why do we need it?
- Avoids displaying unnecessary INFO and WARNING messages.
- Helps engineers focus on application failures.
- Makes troubleshooting easier.

Important Python concepts:
- Empty list
- `append()`
- `if` condition
- `strip()`
- `return`

### Function 4: `analyze_logs(file_path)`

**Purpose:** Combine all functions and generate a consolidated report.

Why do we need it?
- Calls `read_logs()` to read the file.
- Calls `count_log_levels()` to count log levels.
- Calls `find_errors()` to extract errors.
- Displays the final report.

This function acts as the main workflow controller for the log analyzer.

## 6. Issues We Faced During Development

| Issue | Root cause | Resolution |
|---|---|---|
| `python3` command not found | Windows Python launcher uses a different command | Used `py` |
| File not found | Incorrect file path or working directory | Used the script directory to construct the log file path |
| Python code appeared inside log file | Code was accidentally pasted into `application.log` | Restored the correct log content |
| Only one line was read | Used `readline()` instead of `readlines()` | Changed to `readlines()` |
| Function execution issue | Incorrect function indentation/nesting | Corrected function placement and indentation |
| Git push rejected | Remote repository already contained a README commit | Pulled remote changes, merged, and pushed again |

These issues helped us understand Python execution, file handling, directory paths, indentation, and Git collaboration workflows.

## 7. How to Run the Project

Open PowerShell in the project directory.

Run:

```powershell
py "Linux Log Analyzer.py"
```

The script reads `application.log` and displays the analysis report.

## 8. Expected Output

```text
========== PRODUCTION LOG REPORT ==========

Total logs: 8

LOG LEVEL SUMMARY:
INFO: 2
WARNING: 2
ERROR: 4

ERROR DETAILS:
2026-11-01 10:01:02 ERROR Database connection failed
2026-11-01 10:03:04 ERROR API request failed
2026-11-01 10:05:06 ERROR Database connection failed
2026-11-01 10:07:08 ERROR API request failed

============================================
```

## 9. Skills Practiced

- Python functions
- File handling
- Exception handling
- Lists and dictionaries
- Loops and conditional statements
- Linux application log concepts
- PowerShell
- Git and GitHub
- Troubleshooting and debugging

## 10. Future Improvements

- Add timestamps and date-based filtering.
- Detect critical errors automatically.
- Generate reports in CSV format.
- Send alerts when error counts exceed a threshold.
- Analyze large log files efficiently.
- Integrate with monitoring tools such as Grafana and alerting systems.

## 11. Learning Outcome

This project demonstrates how Python can automate a basic SRE task.

The main objective is not just to write Python code, but to understand how engineers can reduce manual production troubleshooting through automation.
