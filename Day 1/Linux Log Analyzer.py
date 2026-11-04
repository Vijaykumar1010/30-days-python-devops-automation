# Linux Log Analyzer

# Objective: Read the application log file using Python.

#def read_logs(file_path):

  #  try: # we use this because file might not exist, or python might encounter a file reading error

  #      with open(file_path, "r") as file:
   #         logs = file.readlines()

   #     return logs
    
    # except FileNotFoundError: # if the file doesnot exist, python handles that error inseated of crashing with an unhandle exception

    #    print("ERROR: log file not found!" )

     #   return [] # returns all collected log entries to whoever call the fuction.


# result = read_logs("application.log")

# print(result)


# Linux Log Analyzer


import os

# Get Python script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Application log file path
LOG_FILE = os.path.join(BASE_DIR, "application.log")


# Function 1: Read application logs
def read_logs(file_path):
    try:
        with open(file_path, "r") as file:
            logs = file.readlines()

        return logs

    except FileNotFoundError:
        print("ERROR: Log file not found!")
        return []


# Function 2: Count the log levels
def count_log_levels(logs):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in logs:
        for level in counts:
            if f" {level} " in line:
                counts[level] += 1

    return counts


# Function 3: Find the error messages
def find_errors(logs):
    errors = []

    for line in logs:
        if "ERROR" in line:
            errors.append(line.strip())

    return errors


# Function 4: Analyze all logs
def analyze_logs(file_path):

    # Step 1: Read logs
    logs = read_logs(file_path)

    # Step 2: Check whether logs are empty
    if not logs:
        print("No logs available for analysis.")
        return

    # Step 3: Calculate total logs
    total_logs = len(logs)

    # Step 4: Count log levels
    summary = count_log_levels(logs)

    # Step 5: Find errors
    errors = find_errors(logs)

    # Step 6: Print final report
    print("\n========== PRODUCTION LOG REPORT ==========")

    print("\nTotal logs:", total_logs)

    print("\nLOG LEVEL SUMMARY:")
    for level, count in summary.items():
        print(f"{level}: {count}")

    print("\nERROR DETAILS:")
    if errors:
        for error in errors:
            print(error)
    else:
        print("No errors found.")

    print("\n============================================")


# Main program
if __name__ == "__main__":
    analyze_logs(LOG_FILE)
