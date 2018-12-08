#This is the PyPoll Homework
#Pulls dependents
import os
import csv

#Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

#list to store data

totalvotes = []
khan = []
correy = []
li = []
otooley = []

#opens the CSV
with open(csvpath, 'r') as csvfile:    
    
    
    #Populates the list
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #total votes
        totalvotes.append(row[0])
        
        if row[2] == "Khan":
            khan.append(str(row[2]))
        elif row[2] == "Correy":
            correy.append(str(row[2]))
        elif row[2] == "Li":
            li.append(str(row[2]))
        elif row[2] == "O'Tooley":
            otooley.append(str(row[2]))     
            
            
    #summarizes all the votes        
    allvotes = len(totalvotes)
    khanvotes = len(khan)/allvotes * 100
    correyvotes = len(correy)/allvotes * 100
    livotes = len(li)/allvotes *100
    otooleyvotes = len(otooley)/allvotes *100

#prints the output
print("----------------")
print(f"total votes were {allvotes}")
print("----------------")
print(f"Khan: {str('%.2f' % (khanvotes))}% ({len(khan)})")
print(f"Correy: {str('%.2f' % (correyvotes))}% ({len(correy)})")
print(f"Li: {str('%.2f' % (livotes))}% ({len(li)})")
print(f"O'Tooley: {str('%.2f' % (otooleyvotes))}% ({len(otooley)})")
print("----------------")
print("Winner: Kahn")
