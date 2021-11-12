# import dependencies

import csv
import os

# path to collect data from resources folder

financial_analysis = os.path.join("resources", "budget_data.csv")

# set variables

date = []
profit = []
change_profit = []

# open csv

with open(financial_analysis) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# read header row and see if it prints
    csv_header = next(csv_reader)
# print(csv_header)

# going through each row
    for row in csv_reader:
        date.append(row[0])
        profit.append(int(row[1]))
    for x in range(len(profit)-1):
        change_profit.append(profit[x+1] - profit[x])

greatest_inc = max(change_profit)
greatest_dec = min(change_profit)

month_inc = change_profit.index(max(change_profit))+1
month_dec = change_profit.index(min(change_profit))+1


print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months:{len(date)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: ${round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {date[month_inc]} (${(str(greatest_inc))})")
print(f"Greatest Decrease in Profits: {date[month_dec]} (${(str(greatest_dec))})")

with open("Export.txt", "w") as export_file:
    export_file.write("Financial Analysis\n")
    export_file.write("-----------------------------------\n")
    export_file.write(f"Total Months:{len(date)}\n")
    export_file.write(f"Total: ${sum(profit)}\n")
    export_file.write(f"Average Change: ${round(sum(change_profit)/len(change_profit),2)}\n")
    export_file.write(f"Greatest Increase in Profits: {date[month_inc]} (${(str(greatest_inc))})\n")
    export_file.write(f"Greatest Decrease in Profits: {date[month_dec]} (${(str(greatest_dec))})\n")

    export_file.close()

