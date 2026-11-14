
import os

# Directory to scan
DIRECTORY = "C:/Users/vijay/Downloads"

# File size threshold (100 MB)
THRESHOLD = 100 * 1024 * 1024

print("Starting Large File Detector...")
print(f"Scanning directory: {DIRECTORY}")
print("-" * 50)

for root, directories, files in os.walk(DIRECTORY):

    for file in files:

        file_path = os.path.join(root, file)

        try:
            # Get file size in bytes
            file_size = os.path.getsize(file_path)

            # Check if file exceeds threshold
            if file_size > THRESHOLD:

                size_mb = file_size / (1024 * 1024)

                print(f"Large File: {file_path}")
                print(f"File Size: {size_mb:.2f} MB")
                print("-" * 50)

        except (PermissionError, FileNotFoundError) as error:
            print(f"Skipping: {file_path} - {error}")

print("Scan completed!")
