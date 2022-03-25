# PART 1
from dataclasses import replace


input_file = open('AoC_day_1_input.txt')
item_list = input_file.readlines()


def depth_counter():
    t = 1
    total = 0
    item_list[0] = item_list[0].replace('\n', '')
    for i in range(0, 1999):
        item_list[t] = item_list[t].replace('\n', '')
        if int(item_list[t]) > int(item_list[t-1]):
            total += 1
        t += 1
    return total


print(depth_counter())


# PART 2


def depth_counter2():
    t = 0
    total = 0
    while True:
        try:
            for i in range(0, 1999):
                item_list[t] = item_list[t].replace('\n', '')
                t += 1
            t = 0
            for i in range(0, 1999):
                window1 = int(item_list[t]) + \
                    int(item_list[t+1]) + int(item_list[t+2])
                window2 = int(item_list[t+1]) + \
                    int(item_list[t+2]) + int(item_list[t+3])
                if window2 > window1:
                    total += 1
                t += 1
        except IndexError:
            break
    return total


print(depth_counter2())
