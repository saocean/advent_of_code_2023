#!/usr/bin/env python3

import re

sum = 0

with open('./1.txt') as file:
    for line in file:
        number_list = [number for number in re.findall(r'\d', line)]
        calibration_value = number_list[0] + number_list[-1]
        sum += int(calibration_value)
    print(sum)
