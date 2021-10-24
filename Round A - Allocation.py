# I have taken silly measures to try and get it on one line but couldn't work out how to deal with the order of the
# inputs in the single line so had to put it in 2 lines instead

import numpy as np
Cases = int(input())
for case in range(0,Cases):
    [num,budget] = [int(s) for s in input().split(' ')]
    print('Case #'+str(case+1)+': '+str(list(np.where(np.sort(np.append(np.cumsum(np.sort([int(s) for s in input().split(' ')])),budget))==budget))[0][-1]))
