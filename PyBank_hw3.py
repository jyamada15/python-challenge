
import csv
import os


os.chdir("C:\\Users\\Jeff\\Documents\\BootCamp\\USCRepository\\USCLOS201805DATA1-Class-Repository-DATA\\02-Homework\\03-Python\\Instructions\\PyBank\\raw_data")
csv_path=os.path.join('..','raw_data','budget_data_1.csv')


file = open(csv_path, newline='')
csv_reader = csv.reader(file)

header = next(csv_reader) # the first line is the header
dset = []
revenue = []
for row in csv_reader:
   date = row[0]
   rev = float(row[1])
   dset.append([date])
   revenue.append([rev])


total_months = len(dset)

def total_rev(revenue):
 total = 0
 for x in revenue:
   total +=sum(x)
 return total


rev_change= []
for j in range(1,len(revenue)):
   rev_change.append(sum(revenue[j]) - sum(revenue[j - 1]))


avg_rev_change = sum(rev_change)/len(rev_change)
max_rev_change = (float(max(rev_change)))
min_rev_change = (float(min(rev_change)))
max_rev_change_date = dset[rev_change.index(max(rev_change))]
min_rev_change_date = dset[rev_change.index(min(rev_change))]


print("Financial Analysis")
print("------------------------------------------")
print("Total Months:  " + str(total_months))
print("The total revenue: " + '${:,.2f}'.format(total_rev(revenue)))
print("Greatest Increase in Revenue: " + str(max_rev_change_date[0]) + "  (" + '${:,.2f}'.format(max_rev_change) + ")")
print("Greatest Decrease in Revenue: " + str(min_rev_change_date[0]) + "  (" + '${:,.2f}'.format(min_rev_change) + ")")


Financial_results = ["Financial Results"]
separator = ["-------------------------"]
Total_months= ["Total Months:  " + str(total_months)]
Total_rev = ["The total revenue: " + '${:,.2f}'.format(total_rev(revenue))]
max_rev = ["Greatest Increase in Revenue: " + str(max_rev_change_date[0]) + "  (" + '${:,.2f}'.format(max_rev_change) + ")"]
min_rev = ["Greatest Decrease in Revenue: " + str(min_rev_change_date[0]) + "  (" + '${:,.2f}'.format(min_rev_change) + ")"]


output_file = os.path.join("C:\\Users\\Jeff\\Documents\\BootCamp\\USCRepository\\USCLOS201805DATA1-Class-Repository-DATA\\02-Homework\\03-Python\\Instructions\\PyBank\\raw_data\\output.txt")
with open(output_file, 'w', newline= '') as datafile:
   writer = csv.writer(datafile)
   writer.writerow(Financial_results)
   writer.writerow(separator)
   writer.writerow(Total_months)
   writer.writerow(Total_rev)
   writer.writerow(max_rev)
   writer.writerow(min_rev)


