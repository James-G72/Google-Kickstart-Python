# This passes for all cases

import numpy as np
# Brute force
Cases = int(input())
for case in range(0,Cases):
    length = int(input())
    array = [int(s) for s in input().split(' ')]
    dif = np.zeros((length-1))
    for x in range(0,length-1):
        dif[x] = array[x]-array[x+1]
    max_dif = 0
    counter = 0
    for x in range(0,len(dif)-1):
        if dif[x] == dif[x+1]:
            counter += 1
        else:
            if counter + 2 > max_dif:
                max_dif = counter + 2
            counter = 0
    if counter+2 > max_dif:
        max_dif = counter+2

    print("Case #"+str(case+1)+": "+str(max_dif))
