# Add our dependencies

import csv
import os

# Assign a variable for the file to load from path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable for the file to save to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

# Read and print the header row
headers = next(file_reader)

print(headers)
