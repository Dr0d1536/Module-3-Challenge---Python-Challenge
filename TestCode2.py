# Python Challenge
import os
import csv


TotalProfit = 0
MonthCount = 0
AverageProfit = 0
AverageTotal = 0

change = 0
value = 0
profit = []


budgetData = os.path.join("budget_data.csv")

with open(budgetData) as dataFile:
    dataReader = csv.reader(dataFile, delimiter=',')
    dataHeader = next(dataReader)
    FirstRow = next(dataReader)
    MonthCount = MonthCount + 1
    TotalProfit += int(FirstRow[1])

    for row in dataReader:
        TotalProfit += int(row[1])
        MonthCount = MonthCount + 1

        change = int(row[1])-value
        profit.append(change)
        value = int(row[1])
        avg_change = round(sum(profit)/len(profit), 2)
        
    print(" \nFinancial Analysis\n___________________\n")
    print("Total Months: "+ str(MonthCount))
    print("Total: $" + str(TotalProfit))
    print("Average Change: $" + str(avg_change))
