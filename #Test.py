import os
import csv

budgetData = os.path.join("budget_data.csv")

NumberOfMonths = []
MonthCount = 0
MoneyMade = []
TotalProfit = 0
#ChangesByMonthBalance = 0
ChangesByMonth = []
Starting = 0
TotalBalance = 0
Total = 0
NewAvg = []
Luck = 0
Neg = 0
Pos = 0
x = []

with open(budgetData) as dataFile:
    dataReader = csv.reader(dataFile, delimiter=',')
    dataHead = next(dataReader)   

    for row in dataReader:
        
        TotalProfit += int(row[1])
        MonthCount = MonthCount + 1

    print(" \nFinancial Analysis\n___________________\n")
    print("Total Months: "+ str(MonthCount))
    print("Total: $" + str(TotalProfit))
   






