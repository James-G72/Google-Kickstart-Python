# This times out on the tests but I'm not sure why
# The logic seems sound and it passes the examples very quickly

import numpy as np
Cases = int(input())
for case in range(0,Cases):
    result = None
    nums = input()
    nums = [int(s) for s in nums.split(' ')]
    R,C = nums
    Wall = np.chararray((R,C))
    for row in range(0,R):
        whole = str(input())
        for column in range(0,C):
            Wall[row,column] = whole[column]
    # At this point we have the wall in a nicer format
    uniques = np.unique(Wall) # List of all the letters we have
    list = [str(uniques[x])[2] for x in range(0,len(uniques))]
    for test in list: # Checking which candidates are suitable to be the first one down
        Pass = 1  # If this boolean survives all the tests then we're good
        for column in range(0,C): # Through all columns
            arm = 0
            for row in np.arange(R,0,-1): # Counting backwards down all the rows
                if arm: # If we have found a value in the column that isn't the test value
                    if str(Wall[row-1,column])[2] == test:
                        Pass = 0 # Then it isn't properly supported
                else:
                    if str(Wall[row-1,column])[2] != test:
                        arm = 1 # We have got one in this row so we want to check
        if Pass:
            result = [test]
    # So now we know which one is the first value
    # If no first value was found then we need to just return a -1
    if result is None:
        result = -1 # The we couldn't start the process and have no first value
    else: # Then we continue to look for results
        while len(result) < len(list):
            for test in list:  # Checking which candidates are suitable to be the first one down
                Pass = 1  # If this boolean survives all the tests then we're good
                for column in range(0,C):  # Through all columns
                    arm = 0
                    for row in np.arange(R,0,-1):  # Counting backwards down all the rows
                        if arm:  # If we have found a value in the column that isn't the test value
                            if str(Wall[row-1,column])[2] == test:
                                Pass = 0  # Then it isn't properly supported
                        else:
                            if str(Wall[row-1,column])[2] != test:
                                if str(Wall[row-1,column])[2] not in result:
                                    arm = 1  # We have got one in this row so we want to check
                if Pass:
                    if test not in result:
                        result.append(test)
    if isinstance(result,int):
        print('Case #'+str(case+1)+': '+str(result))
    else:
        print('Case #'+str(case+1)+': '+''.join(result))
