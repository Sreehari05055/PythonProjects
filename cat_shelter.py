#!/usr/bin/env python3
import sys
from statistics import mean
def ours_and_theirs():
    with open(file_name, 'r') as f:
        for line in f:
            if line == 'END':
                break
            a, b, c = line.strip().split(',')
            difference = int(c)-int(b)
            status = a, difference
            if a == 'OURS':
                list_1.append(difference)
            else:
                list_2.append(status)
    return

def time_conversion(sum_1):
    hours = sum_1 // 60
    minutes = sum_1 % 60
    hours_word = 'hours' if hours > 1 else 'hour'
    minutes_word = 'minutes' if minutes > 1 else 'minutes'
    return f'{hours} {hours_word}, {minutes} {minutes_word}'

if __name__ == '__main__':
    
    while True:
        file_name = input(f'filename: {sys.argv[0]}')
        try:
            list_1 = []
            list_2 = []

            ours_and_theirs()

            sum_1 = sum(list_1)
            count_1 = len(list_1)
            count_2 = len(list_2)

            print('Log File analysis')
            print('=================')
            print(f'Cat visits: {str(count_1)}')
            print(f'Other cats: {str(count_2)}')
            print('')
            print(f'Total time in house: {time_conversion(sum(list_1))}')
            print('')
            print(f'Average visit length:  {time_conversion(round(mean(list_1)))}')
            print(f'Longest visit:         {time_conversion(max(list_1))}')
            print(f'Shortest visit:        {time_conversion(min(list_1))}')
        except FileNotFoundError:
            print('File not found')
            continue
        break
