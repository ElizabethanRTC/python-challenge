import csv
import os

pwd = os.path.abspath('.')

csvpath = os.path.join(pwd, 'election_data.csv')


rowCount = 0 
candidateVote = {}

with open(csvpath) as electionData:
    csvReader = csv.reader(electionData)
    fields = next(csvReader)

    for row in csvReader:
        rowCount = rowCount + 1
        cName = row[2] 
        if cName in candidateVote: 
            candidateVote[cName] = candidateVote[cName] + 1
        else:
            candidateVote[cName] = 1

print("----------------------")
print("Total votes:", rowCount)
print("----------------------")

winner = ""
maxCount = 0

for cName in candidateVote:
    print(cName + "\t" + str(round(candidateVote[cName]*100/rowCount))+ "%\t" + str(candidateVote[cName]))
    if candidateVote[cName] > maxCount:
       winner = cName
       maxCount = candidateVote[cName]

print("--------------------")
print("Winner: " + winner)
print("--------------------")

outputFile = open("output.txt", "w")

outputFile = open("output.txt", "w")

outputFile.write("-------------------")
outputFile.write("Total votes: " + str(rowCount) + "\n")
outputFile.write("-------------------")
