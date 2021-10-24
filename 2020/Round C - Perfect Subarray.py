# Unlike with most kickstart problems the brute force method doesn't work as it takes too long for even test set 1
# This file represents the fastest I could get the brute force method to work and it still times out
# The logic however is correct

import math
Cases = int(input())
for case in range(0,Cases):
    length = int(input())
    array = [int(x) for x in input().split()]
    result = 0
    max_number = sum([x for x in array if x > 0])
    squares = [x**2 for x in range(0,math.floor(math.sqrt(max_number))+1)]
    for start in range(0,len(array)): # Through all possible start-points
        summation = 0
        for consider in array[start:]: # Through all end-points
            summation += consider
            if summation in squares:
                result += 1
    print('Case #'+str(case+1)+': '+str(result))
