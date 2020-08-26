import csv
import os
filepath = os.path.join('Resources', 'budget_data.csv')

with open(filepath) as file:
    reader = csv.reader(file)  
    # skip header row
    next(reader)
    
    n_months = 0
    total_profit_losses = 0
    profit_losses = []
    months = []
    
    for row in reader:
        n_months += 1
        total_profit_losses += int(row[1])
        profit_losses.append(int(row[1]))
        months.append(row[0])

    differences = []
    for i in range(1, len(profit_losses)):
        differences.append(profit_losses[i] - profit_losses[i-1])
    avg_change = sum(differences)/len(differences)
             
    greatest_increase = max(differences)
    month_greatest_increase = months[differences.index(greatest_increase)+1]
    
    greatest_decrease = min(differences)
    month_greatest_decrease = months[differences.index(greatest_decrease)+1]

print('Total Months:', n_months)
print('Total: $', total_profit_losses)
print('Average Change: $', round(avg_change,2))
print('Greatest Increase in Profits', month_greatest_increase, greatest_increase)
print('Greatest Decrease in Profits', month_greatest_decrease, greatest_decrease)

results_filepath = os.path.join('analysis', 'results.txt')
with open(results_filepath, 'w') as file:
    file.write('Total Months: '+ str(n_months) + '\n')
    file.write('Total: $' + str(total_profit_losses) + '\n')
    file.write('Average Change: $' + str(round(avg_change,2)) + '\n')
    file.write('Greatest Increase in Profits ' + month_greatest_increase + ' ' + str(greatest_increase) + '\n')
    file.write('Greatest Decrease in Profits ' + month_greatest_decrease + ' ' + str(greatest_decrease))
