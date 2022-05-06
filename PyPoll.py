# Add our dependencies

import csv
import os

# Assign a variable for the file to load from path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable for the file to save to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0

#Print the candidate name from each row
candidate_options = []

#1 Declare the empty dictionary
candidate_votes = {}

# Winning candidate and winning count tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.

    for row in file_reader:

        # Add to the total vote count
        
        total_votes += 1

        #3. Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)

            #2 begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidates count
        candidate_votes[candidate_name] += 1

# print the candidate list

print(candidate_options)

# Determine the percentage of votes for each candidate by looping through the counts

#1 iterate thru the candidate list
for candidate_name in candidate_votes:
    #2 retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #3 calculate percent of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # to do: print out each candidates name, vote count, and percentage of
    # votes to the terminal

    print(f"{candidate_name}: {vote_percentage:.1f}%({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count = votes and winning_percent = 
        # vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # and, set the winning_candidate equal to the candidate name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
# To do: print out the winning candidate, vote count and percentage to
# terminal