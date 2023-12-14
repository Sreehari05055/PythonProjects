#!/usr/bin/env python3
import sys
from statistics import mean

file_name = input(f'filename: ' + sys.argv[0])

list_1 = []
list_2 = []

with open(file_name, 'r') as f:
    file = f.read()
    f.close()

mods = file.replace(('END'),(''))
with open(file_name, 'w') as f:
    f.write(mods)
    f.close()

def ours_and_theirs():
    with open(file_name, 'r') as f:
        for line in f:
            a, b, c = line.strip().split(',')
            difference = int(c)-int(b)
            status = a, difference
            if a == 'OURS':
                list_1.append(difference)
            else:
                list_2.append(status)
    return
ours_and_theirs()

sum_1 = sum(list_1)
hours = sum_1 // 60
minutes = sum_1 % 60
count_1 = len(list_1)
count_2 = len(list_2)
maximum_value = max(list_1)
minimum_value = min(list_1)
average = mean(list_1)

print('Log File analysis')
print('=================')
print(f'Cat visits: '+str(count_1))
print(f'Other cats: '+str(count_2))
print(f'')
print(f'Total time in house: '+ str(hours)+' hours, ' + str(minutes)+' minutes')
print(f'')
print(f'Average visit length:'+ str(round(average)) +' minutes')
print(f'Longest visit:       '+ str(maximum_value) +' minutes')
print(f'Shortest visit:      '+ str(minimum_value) +' minutes')