# This is the fully optimised solution for the plates problem
# Unfortuately it still doesn't pass test case 2 as it takes too long to do the very large cases

import numpy as np
import itertools

def Permutations(N,K,P,numbers): # This returns a numpy array of possible options for how you could select plates
    full = [seq for seq in itertools.permutations(numbers,N) if sum(seq) == P]
    sets = set(full)
    return sets

Cases = int(input())
for case in range(0,Cases):
    [N,K,P] = [int(s) for s in input().split(' ')]
    hold = np.zeros((N,K+1)) # We add an extra line of zeros to represent 0 plates taken from that stack
    for stack in range(0,N):
        hold[stack,1:] = [int(s) for s in input().split(' ')]  # Input is top to bottom of the stack
    cumulative = hold.cumsum(axis=1)
    # We now have all of the stacks in a single array
    # Approach taken is to just sum each possibility
    max_value = 0  # Tracker for the result
    # This is going to have to be much cleverer
    if P == 1:
        max_value = max(cumulative[:,1]) # Taking the first row as we only need the largest of the top plates
    elif P == N*K:
        max_value = sum(cumulative[:,K])
    else: # Then we have to do some more complex logic
        numbers = []  # Empty list
        for x in range(0,K+1):
            for i in (0,K+1):
                numbers.append(x)
        sets = Permutations(N,K,P,numbers) # This gives us all the possible combinations that would give us enough plates
        for check in sets:
            value = 0
            for x in range(0,N): # Through all stacks
                value += cumulative[x,check[x]]
            if value > max_value:
                max_value = value

    print('Case #'+str(case+1)+': '+str(int(max_value)))
