import sys

if __name__ == "__main__":
    num_lines = int(input().strip())
    my_input = []
    for my_input_i in range(num_lines):
        my_input_t = [int(my_input_temp) for my_input_temp in input().strip().split(' ')]
        my_input.append(my_input_t)


    def getkey(item):
        return item[1]


    data = sorted(my_input, key=getkey)

    end_times = []
    start_times = []
    for row in data:
        end_times.append(row[3])
        start_times.append(row[2])

    end_time_min = max(end_times)
    start_time_min = min(start_times)
    total_time = end_time_min - start_time_min + 1

    output = [0 for i in range(total_time)]

    for row in data:
        target_id = row[0]
        start_time = row[2] - start_time_min
        end_time = row[3] - start_time_min
        for idx in range(start_time, end_time + 1):
            output[idx] = target_id
    for idx in range(len(output)):
        print(str(idx + start_time_min) + ': ' + str(output[idx]))
