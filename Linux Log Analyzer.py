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
def count_log_levels(logs):
        counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0     
        }

        for line in logs:
            for level in counts:
                if f" { level} " in line:
                    counts[level] +=1
        return counts

# Main program
if __name__ == "__main__":
    
    # Function 1: Read logs
    logs = read_logs(LOG_FILE)

    print("Total logs:", len(logs))

    # Function 2: Count log levels
    result = count_log_levels(logs)

    print("Log Summary:", result)