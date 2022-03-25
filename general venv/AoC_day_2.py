from dataclasses import replace
import re

input_file = open('AoC_day_2_input.txt')
item_list = input_file.readlines()


def depth_counter2():
    forward = 0
    depth = 0
    while True:
        try:
            for item in range(0, 1000):
                item_list[item] = item_list[item].replace('\n', '')
        except IndexError:
            break
    while True:
        try:
            for i in range(0, 1000):
                num = re.compile(r'\d+')
                if re.search('forward', item_list[i]) == True:
                    forward += int(num.search(item_list[i]).group(1))
                if re.search('down', item_list[i]) == True:
                    depth += int(num.search(item_list[i]).group(1))
                if re.search('up', item_list[i]) == True:
                    depth -= int(num.search(item_list[i]).group(1))
        except IndexError:
            break
    return forward * depth


depth_counter2()
print(item_list)
