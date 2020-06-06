# The first test case is very easy but the second times out
# This solution works but is intensive

import math
Cases = int(input())
for case in range(0,Cases):
    [N,K] = [int(s) for s in input().split(' ')]
    array = [int(s) for s in input().split(' ')]
    Differences = [array[x+1]-array[x] for x in range(0,len(array)-1)] # Calculating the difference between each of the
    live_array = array
    for x in range(0,K): # This is how many workouts we're allowed to add
        New_Point = live_array[Differences.index(max(Differences))]+math.ceil(max(Differences)/2) # This is the equivalent of the workout being added
        live_array.append(New_Point)
        live_array.sort()
        Differences = [live_array[x+1]-live_array[x] for x in range(0,len(live_array)-1)]
        Difficulty = max(Differences) # If its odd then it goes up


    print('Case #'+str(case+1)+': '+str(Difficulty))
