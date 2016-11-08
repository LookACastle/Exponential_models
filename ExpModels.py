# -*- coding: utf-8 -*-
#import visual
#import visual.graph
import time # For optimisation and bugtesting purposes

start = time.time()

temp_data = [15, 16, 18, 19, 22, 24, 31, 42, 49, 67, 78, 90, 105, 109, 122, 125]

for i in range(len(temp_data) - 1):
    percent_increase = 100 / temp_data[i] * temp_data[i + 1] - 100
    print(percent_increase)

end = time.time()

print("it took: ", end - start, "seconds to do this")
