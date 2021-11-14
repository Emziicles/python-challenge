# declare dependencies

import os
import csv

# create file path for csv

election_data = os.path.join("resources", "election_data.csv")

# read the csv file
with open (election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# read header row
    csv_header = next(csv_reader)

# declare variables

    total_votes = 0
    candidate_list = []
    candidate_votes = {}
    winner_count = 0


    for row in csv_reader:
        total_votes += 1

        if row[2] not in candidate_votes.keys():
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1

print("Election Results")
print("----------------------------")
print(f"Total number of votes: {[total_votes]}")
print("----------------------------")

candidates_info = ""
for candidates in candidate_votes.keys():
    candidates_info = '\n'.join([candidates_info, candidates + " {:.2%}".format(candidate_votes[candidates] / total_votes) + "("+ str(candidate_votes[candidates])+ ")\n"])
print(candidates_info)


winner = max(candidate_votes, key=candidate_votes.get)

print("----------------------------")
print(f"Winner: {[winner]}")
print("----------------------------")

# write into new text file

with open("Poll_Export.txt", "w") as export_file:
    export_file.write("Election Results\n")
    export_file.write("----------------------------\n")
    export_file.write(f"Total number of votes: {[total_votes]}\n")
    export_file.write("----------------------------\n")
    export_file.write(f"{[candidates_info]}\n")
    export_file.write("----------------------------\n")
    export_file.write(f"Winner: {[winner]}\n")
    export_file.write("----------------------------\n")

    export_file.close()




