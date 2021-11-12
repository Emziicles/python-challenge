# declare dependencies
import os
import csv

# path to collect data from resources folder

election_data = os.path.join("resources", "election_data.csv")

# set variables

total_votes = 0

# open csv

with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# read header row
    csv_header = next(csv_reader)


