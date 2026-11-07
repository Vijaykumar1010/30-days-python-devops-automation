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


# function call

check_disk_usage()