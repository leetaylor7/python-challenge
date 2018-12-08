#This is the Banking Homework
#Pulls dependents
import os
import csv

#Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

#list to store data

months = []
profits = []
change = []

#opens the CSV
with open(csvpath, newline='') as csvfile:    
    #Populates the list
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #add month
        months.append(row[0])
        profits.append(float(row[1]))
    
    #Prints questions 1 and 2
    print(f"There are {len(months)}")
    print(f"Total profits are ${sum(profits)}")
    
    
    #compiles list for questions 3 - 5
    for i in range(1, len(profits)):
        changes = profits[i] - profits[i - 1]
        change.append(float(changes))
    
    #finds the average
    average = sum(change)/len(change)
    print(f"the average change is: {average}")
    print(f"the max is {max(change)}")
    print(f"the min is {min(change)}")
    

