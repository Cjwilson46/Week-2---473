# alharthiD_WK2-2_script.py
# Name: Christopher Wilson
# Date: 1/20/24
# Assignment: WK2-2

import os
import hashlib

# Function to calculate MD5 hash of a file
def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Directory to traverse - replace with the desired directory
directory = "."

fileHashes = {}

# Walking through the directory
for root, dirs, files in os.walk(directory):
    for fileName in files:
        path = os.path.join(root, fileName)
        fullPath = os.path.abspath(path)

        # Calculating MD5 hash for each file
        fileHash = calculate_md5(fullPath)
        fileHashes[fileHash] = fullPath

# Printing the results in a standard format
print("{:<40} {:<}".format('MD5 Hash', 'File Path'))
for hash, path in fileHashes.items():
    print("{:<40} {:<}".format(hash, path))

# End of script

        
