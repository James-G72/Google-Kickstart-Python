# The logic is fully implimented and if General_Case is set to True then it uses the full solution instead of the cheaty one

import numpy as np
import itertools

def Permutations(N,K,P): # This returns a numpy array of possible options for how you could select plates
    numbers = [] # Empty list
    for x in range(0,K+1):
        for i in (0,K+1):
            numbers.append(x)
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
    General_Case = True # This allows the general case and the specific case to be chosen between
    if not General_Case and N <= 3: # If we can use the specific case
        if P == 1: # This way we know that P isn't 1 for all logic below
            max_value = max(cumulative[:,1]) # Taking the first row as we only need the largest of the top plates
        elif N == 1: # Simplest case
            max_value = max(cumulative[:,P]) # Then we just take how many plates we need
        elif N == 2:
            for stack_1 in range(0,K+1): # Stack 1 starts empty
                for stack_2 in range(0,K+1): # Stack 2 starts full
                    if stack_1+stack_2 == P: # This is just lazy but will only do the sum for valid combinations
                        if cumulative[0,stack_1]+cumulative[1,stack_2] > max_value:
                            max_value = cumulative[0,stack_1]+cumulative[1,stack_2]
        elif N == 3:
            for stack_1 in range(0,K+1): # Stack 1 starts empty
                for stack_2 in range(0,K+1): # All stacks start empty
                    for stack_3 in range(0,K+1):
                        if stack_1+stack_2+stack_3 == P: # This is just lazy but will only do the sum for valid combinations
                            if cumulative[0,stack_1]+cumulative[1,stack_2]+cumulative[2,stack_3] > max_value:
                                max_value = cumulative[0,stack_1]+cumulative[1,stack_2]+cumulative[2,stack_3]
    else: # If General_Case is set to True then this will be used for all cases
        # This is going to have to be much cleverer
        if P == 1:
            max_value = max(cumulative[:,1]) # Taking the first row as we only need the largest of the top plates
        elif P == N*K:
            max_value = sum(cumulative[:,K])
        else: # Then we have to do some more complex logic
            # Hoping it is quick enough to calculate all options and check them - maybe eventually all options could be calculated and checked simultaneously
            sets = Permutations(N,K,P) # This gives us all the possible combinations that would give us enough plates
            for check in sets:
                value = 0
                for x in range(0,N): # Through all stacks
                    value += cumulative[x,check[x]]
                if value > max_value:
                    max_value = value

    print('Case #'+str(case+1)+': '+str(int(max_value)))
