# Add our dependencies

import csv
import os

# Assign a variable for the file to load from path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable for the file to save to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate options and Candidate votes
candidate_options = []

candidate_votes = {}

# Track Winning candidate, vote count, and percentage

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

        # Get the candidate name from each row

        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)

            # begin tracking that candidates voter count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidates count
        candidate_votes[candidate_name] += 1

# save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts

    # iterate thru the candidate list
    for candidate_name in candidate_votes:
        # retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # calculate percent of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # print each candidate's voter count and percent to terminal

        print(candidate_results)

        # save the candidate results to our text file

        txt_file.write(candidate_results)
        # Determine winning vote count and candidate and percent
        # Determine if the votes is greater than the winning count

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percent = 
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # and, set the winning_candidate equal to the candidate name
            winning_candidate = candidate_name

    # print the winning candidate's results to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # save winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)