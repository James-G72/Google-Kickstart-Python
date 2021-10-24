# This passes for all cases - not yet
import math
import pandas as pd

Cases = int(input())
for case in range(0,Cases):
    number, max = [int(s) for s in input().split(' ')]
    withdraw = [int(s) for s in input().split(' ')]
    leave_list = ""
    div = 10000000000
    minor = [x % max for x in withdraw]
    major = pd.Series([math.floor(withdraw[x]/max)-minor[x]/div for x in range(0, number)]).sort_values(ascending=True)
    for x in major.index:
        leave_list += " " + str(x+1)

    print("Case #"+str(case+1)+":"+leave_list)
