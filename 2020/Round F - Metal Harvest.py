# This passes for all cases - not yet
import math

def harvest(array, limit):
    if not len(array):
        return 0
    result = 0
    array.sort()
    s,e = -1,-1

    for start,end in array:
        # Checking if the range can be covered by the previous robot as well
        if e <= start or start < e < end:
            pos = max(start,e)
            times = math.ceil((end-pos) / limit)
            s = pos+(times-1) * limit
            e = s + limit
            result += times
    return result

Cases = int(input())
for case in range(0,Cases):
    number, maxim = [int(s) for s in input().split(' ')]
    times = []
    for x in range(0,number):
        times.append([int(s) for s in input().split(' ')])
    deploys = harvest(times, maxim)

    print("Case #"+str(case+1)+": "+str(deploys))

