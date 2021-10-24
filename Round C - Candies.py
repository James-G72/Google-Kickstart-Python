# This uses matrices to solve the problems without having to use a for loop which is problematic for large tasks

import numpy as np
Cases = int(input())
for case in range(0,Cases):
    [N,Q] = [int(s) for s in input().split(' ')]
    array = np.array([int(s) for s in input().split(' ')])
    score = 0
    comp = []
    for x in range(0,N):
        if x % 2 == 0:
            comp.append(x+1)
        else:
            comp.append(-(x+1))
    comp = np.array(comp).transpose()
    for task in range(0,Q): # Collecting inputs
        [Q_U,start,end] = input().split(' ')
        start = int(start)
        end = int(end)
        if Q_U == 'Q':
            score += sum(array[start-1:end]*comp[0:(end-start)+1])
        else: # Update a value
            array[start-1] = end
    print('Case #'+str(case+1)+': '+str(score))
