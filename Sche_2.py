# <target_id> <priority> <time> <x_location> <y_location>
my_input = [[0, 1, 0, 0, 4], [0, 1, 1, 0, 5], [1, 2, 1, 3, 6], [1, 2, 2, 3, 6], [2, 3, 3, -6, 4], [2, 3, 4, -7, 3]]

# !/bin/python3

import sys
import random


def getkey(item):
    return item[2]


def data_time(data, time):
    data_in_range = []
    for row in data:
        if time == row[2]:
            data_in_range.append(row)
        else:
            pass
    return data_in_range


def max_blimp_in_range(data, time, point):
    data_in_range = []
    for row in data:
        if abs(row[3] - point[0]) <= 5 and abs(row[4] - point[1]) <= 5 and time == row[2]:
            data_in_range.append(row)
        else:
            pass
    max_blimp = max(data_in_range, key=lambda i: i[1])
    return max_blimp


def random_step():
    return random.choice([[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1], [0, 0]])


data = sorted(my_input, key=getkey, reverse=True)
times = []
current_loc = [0, 0]

for row in data:
    times.append(row[2])

end_time = max(times)
start_time = min(times)
total_time = end_time - start_time + 1

output = [[-1, 0, 0] for i in range(total_time)]

for idx in range(len(output)):
    try:
        if idx == 0:
            blimp = max_blimp_in_range(data, idx + start_time, current_loc)
        else:
            blimp = max_blimp_in_range(data, idx + start_time, current_loc + random_step())
    except:
        blimp = [-1] + [0 for i in range(4)]
    print(str(idx + start_time) + ': ' + '(' + str(blimp[0]) + ',' + str(0) + ',' + str(0) + ')')
