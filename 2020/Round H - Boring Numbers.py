# This passes test case 1 and TLE for test case 2

def boring_check(num):
    str_num = str(num)
    iupg = 1
    for x in range(1,len(str_num)+1):
        if int(str_num[x-1]) % 2 != x % 2:
            iupg = 0
    return iupg

Cases = int(input())
cheat_dict = {}
for case in range(0,Cases):
    L,R = [int(s) for s in input().split(' ')]
    boring = 0
    for x in range(L,R+1):
        if x not in cheat_dict:
            result = boring_check(x)
            cheat_dict[x] = result
            boring += result
        else:
            boring += cheat_dict[x]

    print("Case #"+str(case+1)+": "+str(boring))
