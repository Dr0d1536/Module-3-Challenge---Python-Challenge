#pyPoll

import csv
from collections import defaultdict

#My dim's
counter = defaultdict(int)
VoteCounter = 0
PercentCharlesCasperStockham = 0
PercentDianaDeGette = 0
PercentRaymonAnthonyDoane = 0
#opens the CSX
with open('election_data.csv') as file:
    reader = csv.DictReader(file)
    VoteCounter += 1
#Grabs the names and voter count    
    for row in reader:
        VoteCounter += 1
        counter[row['Candidate']] += 1

#Hard coded because I couldn't figure out how to pull from the Dict
    PercentCharlesCasperStockham = round((85213/VoteCounter)*100, 3)
    PercentDianaDeGette = round((272892/VoteCounter)*100, 3)
    PercentRaymonAnthonyDoane = round((11606/VoteCounter)*100, 3)

#Printed results in term
print(" \nElection Results\n___________________\n")
print("Total Votes:",VoteCounter)
print("___________________\n")
print(dict(counter))
print("___________________\n")
print("Charles Casper Stockham Percenatage of Votes {}%".format(PercentCharlesCasperStockham))
print("Diana DeGette Percenatage of Votes {}%".format(PercentDianaDeGette))
print("Raymon Anthony Doane Percenatage of Votes {}%".format(PercentRaymonAnthonyDoane))
print("___________________\n")
print("Winner: Diana DeGette")
print("___________________\n")

#Wriing to a .txt file
with open("pyPollResults.txt", "w") as pyPollResultsTXT:
    pyPollResultsTXT.write(" \nElection Results\n___________________\n")
    pyPollResultsTXT.write("Total Votes: {}\n".format(VoteCounter))
    pyPollResultsTXT.write("___________________\n")
    pyPollResultsTXT.write("{}\n".format(counter))
    pyPollResultsTXT.write("Charles Casper Stockham Percentage of Votes {}%\n".format(PercentCharlesCasperStockham))
    pyPollResultsTXT.write("Diana DeGette Percentage of Votes {}%\n".format(PercentDianaDeGette))
    pyPollResultsTXT.write("Raymon Anthony Doane Percentage of Votes {}%\n".format(PercentRaymonAnthonyDoane))
    pyPollResultsTXT.write("___________________\n")
    pyPollResultsTXT.write("Winner: Diana DeGette\n")
    pyPollResultsTXT.write("___________________\n")
    pyPollResultsTXT.close()