# -*- coding: utf-8 -*-
from __future__ import division, print_function
from math import *
import vpython
import time # For optimisation and bugtesting purposes

start = time.time()

temp_data = [15, 16, 18, 19, 22, 24, 31, 42, 49, 67, 78, 90, 105, 109, 122, 125]

points = vpython.gdots()

def get_projection_factor(list):
    output = []
    for i in range(len(list) - 1):
        projection_factor = 100 / list[i] * list[i + 1] / 100
        output.append(projection_factor)
    return output

for x in range(len(temp_data)):
    points.plot(x, temp_data[x])

end = time.time()

print("it took: ", end - start, "seconds to do this")
