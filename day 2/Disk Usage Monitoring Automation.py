# Disk Usage Monitoring Automation

# Build a Python script that monitors Linux disk usage and alerts you when a filesystem is running out of space

# Step 1: Import the module

import shutil

# function 1

def check_disk_usage():

    disk = shutil.disk_usage("/")   # check the disk usag of the root filesystem

    total = disk.total  # total disk capacity in byte

    used = disk.used # used disk space in bytes

    free = disk.free # free disk space in bytes

    print("Total:", total)
    print("Used:", used)
    print("Free:", free)

    # Convert bytes into GB
    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)

    print(f"Total Space: {total_gb:.2f} GB")
    print(f"Used Space: {used_gb:.2f} GB")
    print(f"Free Space: {free_gb:.2f} GB")

    # Calculate disk usage percentage
    usage_percent = (used / total) * 100

    print(f"Disk Usage: {usage_percent:.2f}%")

    # Add alerting logic
    if usage_percent >= 80:
         print("WARNING: Disk usage is high!")

    else:
        print("OK: Disk usage is healthy.")


# function call

check_disk_usage()