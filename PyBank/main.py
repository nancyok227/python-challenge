# Create  file paths across operating systems

import os

# module for reading CSVfile

import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Create empty lists to iterate through specific rows in the following variables
total_months = []
total_profit = []
monthly_profit_change = []


with open(budget_csv) as csvfile:

# csv reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

# read the header row first (skip this step if there is now header)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}") 
    for row in csvreader:
        # print(row)
       

# Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

# iterate through the profits in order to get the monthly change in profits
for i in range(len(total_profit)-1):

        # take and record difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# Get the Max and Min of the monthly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)


# Match up Max and Min to the proper month using month list and index from Max and Min
# Add +1 to take care of next month since month associated with change is the +1 month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1


# Print Statements

print(f"Financial Analysis")
print("---------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


# Output files
output_path = os.path.join("Analysis", "Financial_Analysis_Summary.text")

# Open the file using "write" mode. Specify the variable to hold the content
with open(output_path, 'w') as file:

# Write how Financial Analysis Summary should be printed
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-----------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change), 2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
