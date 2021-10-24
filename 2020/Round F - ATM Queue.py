# This passes for all cases
import math
Cases = int(input())
for case in range(0,Cases):
    number, max = [int(s) for s in input().split(' ')]
    withdraw = [int(s) for s in input().split(' ')]
    temp = []
    for i in range(number):
        temp.append([withdraw[i],math.ceil(withdraw[i] / max),i])
    temp.sort(key=lambda x:x[1])
    sorted_list = ""
    for i in temp:
        sorted_list+= " "+str(i[2]+1)

    print("Case #"+str(case+1)+":"+sorted_list)
