# import dependencies

import os

import csv


# Assign file location 
election_csv = os.path.join("Resources", "election_data.csv")

# list of variables

Total_votes = 0
Charles_Casper_Stockham_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_votes = 0

# open csv in default read mode with context manager
with open(election_csv) as csvfile:
    # Store data under the csvreader variable
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # read the header row first...Skip header to iterate through the actual values
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # iterate through each row in the csv
    for row in csvreader:
        # Count the unique Voter ID's and store in variable called Total_votes
        Total_votes +=1

        # there are three candidates, count how many times each candidates name appear and store as list
        # values obtained here can be used for percent vote calculation
        if row[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham_votes +=1

        elif row[2] == "Diana DeGette":
            Diana_DeGette_votes +=1

        elif row[2] == "Raymon Anthony Doane":
            Raymon_Anthony_Doane_votes +=1

# To find the winner, a dictionary needs to be created out of the previous two lists created that is for candidates and votes
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_Casper_Stockham_votes, Diana_DeGette_votes, Raymon_Anthony_Doane_votes]

# Zip two lists created above together with candidate(key) and total votes(values)
# Return the winner using max function of the dictionary
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#Print Summary of analysis
Charles_Casper_Stockham_percent = (Charles_Casper_Stockham_votes/Total_votes) * 100
Diana_DeGette_percent = (Diana_DeGette_votes/Total_votes) * 100
Raymon_Anthony_Doane_percent = (Raymon_Anthony_Doane_votes/Total_votes) * 100


# Print summary table
print(f"Election Results")
print(f"----------------------")
print(f"Total Votes: {Total_votes}")
print(f"----------------------")
print(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
print(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
print(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
print(f"----------------------") 
print(f"Winner: {key}")
print(f"----------------------") 


# Output file
# Assign output file location
output_path = os.path.join("Analysis", "Election_Results_Summary.txt")

# Open the file using "write" mode. Specify the variable to hold the content
with open(output_path, 'w') as file:

# Write and print how Election Results Summary should look
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------")
    file.write("\n")
    file.write(f"Total Votes: {Total_votes}")
    file.write("\n")
    file.write(f"---------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
    file.write("\n")
    file.write(f"---------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"---------------------")