# DAlharthi_WK2-1_script.py
# Name: Christopher Wilson
# Date: 1/19/24
# Assignment: WK2-1

import os

# Open the log file
with open("redhat.txt", 'r') as logFile:
    for eachLine in logFile:
        # Split the line into individual words
        fieldList = eachLine.split()

        # Iterate over each word in the line
        for eachField in fieldList:
            # Check if the word contains 'worm' (case-insensitive)
            if 'worm.' in eachField.lower():
                # Print the entire word which is the worm name
                print(eachField)
