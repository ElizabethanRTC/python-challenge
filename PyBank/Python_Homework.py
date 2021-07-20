import csv
import os



pwd = os.path.abspath('.')
#print(pwd)
csvpath = os.path.join(pwd, 'budget_data.csv')


with open(csvpath) as budgetdata:
    reader = csv.reader(budgetdata)
    # print(type(reader))
    # for row in reader: 
    #     print(row[0], row[1])
    pldata = [(date, money) for date, money in reader][1:]
      
#print(pldata)
total_months = len(pldata)

netprofit = sum(int(money) for date, money in pldata)

profit_diff_list = [(pldata[i + 1][0], int(pldata[i+1][1]) - int(pldata[i][1])) for i in range(len(pldata) - 1)]
average_profit_diff = round(sum(moneydiff for date, moneydiff in profit_diff_list)/ (len(pldata) - 1), 2)

max_profit_diff = 0
max_profit_diff_date = profit_diff_list[0][0]
for date, moneydiff in profit_diff_list:
    if moneydiff > max_profit_diff:
        max_profit_diff = moneydiff
        max_profit_diff_date = date


min_profit_diff = 0
min_profit_diff_date = profit_diff_list[0][0]
for date, moneydiff in profit_diff_list:
    if moneydiff < min_profit_diff:
        min_profit_diff = moneydiff
        min_profit_diff_date = date



output_message = f'''Financial Analysis
-------------------------------------------
Total Months: {total_months}
Total: {netprofit}
Average Change: {average_profit_diff}
Greatest Increase in Profits: {max_profit_diff_date} (${max_profit_diff})
Greatest Decrease in Profits: {min_profit_diff} (${min_profit_diff})
'''
print(output_message)

with open('results.txt', 'w') as results:
    results.write(output_message)





