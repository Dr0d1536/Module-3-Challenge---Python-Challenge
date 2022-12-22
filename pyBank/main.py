#Python Challenge
#Imports used to read CSV File
import os
import csv

#Path to CSV file
budgetData = os.path.join("budget_data.csv")
#Declared varaibles and holders
MonthCounter = 0
Profit = 0
Value = 0
Diff = 0
MonthHolder = []
Money = []

#Opens, reads and recognizes the CSV has a header
with open(budgetData, encoding= 'UTF-8', newline="") as budget_file:
    DataReader = csv.reader(budget_file, delimiter=",")
#Returns the next item in the iterator 
    DataHeader = next(DataReader)
    FirstRow = next(DataReader)
#Counters
    MonthCounter += 1
    Profit += int(FirstRow[1])
    Value = int(FirstRow[1])

    for row in DataReader:

#Captures months in the 1st row of the CSV
        MonthHolder.append(row[0])
        MonthCounter += 1
#Captures changes from the 2nd row of the CSV file
        Diff = int(row[1]) - Value
        Money.append(Diff)
        Value = int(row[1])

        
#Adds the 2nd row from the CSV
        Profit = Profit + int(row[1])
        
#Math for the Average and rounds the results up 2. 
        AverageChange = round(sum(Money)/len(Money),2)

#Takes the max and min from the Money index
    Increase = max(Money)
    Decrease = min(Money)
    IncreaseIndex = Money.index(Increase)
    DecreaseIndex = Money.index(Decrease)
 #Captures the month of the Max an Min   
    IncreaseDate = MonthHolder[IncreaseIndex]
    DecreaseDate = MonthHolder[DecreaseIndex]

#Printing results to the terminal
    print(" \nFinancial Analysis\n___________________\n")
    print("Total Months: ",MonthCounter)
    print("Total: ${}".format(Profit))
    print("Average Change: ${}".format(AverageChange))
    print("Greatest Increase in Profits: {} {}".format(IncreaseDate, Increase))
    print("Greatest Decrease in Profits: {} ({})".format(DecreaseDate, Decrease))

#Wriing to a .txt file
with open("ProfitandLosses.txt", "w") as ProfitandLossesTxT:
    ProfitandLossesTxT.write(" \nFinancial Analysis\n___________________\n\n")
    ProfitandLossesTxT.write("Total Months: {} \n".format(MonthCounter))
    ProfitandLossesTxT.write("Total Months: {} \n".format(Profit))
    ProfitandLossesTxT.write("Total Months: {} \n".format(AverageChange))
    ProfitandLossesTxT.write("Greatest Increase in Profits: {} {} \n".format(IncreaseDate, Increase))
    ProfitandLossesTxT.write("Greatest Decrease in Profits: {} ({})".format(DecreaseDate, Decrease))
    ProfitandLossesTxT.close()