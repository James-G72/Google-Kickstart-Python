# This is a mess because i wrote it when i really didn't understand the inputs
# It works though.....

Cases = int(input())
for case in range(0,Cases):
    info = [int(s) for s in input().split(' ')]
    array = [int(s) for s in input().split(' ')]
    limit = info[1]
    unsolved = True
    days = limit
    if len(array) > 1:
        count = len(array)-1
    else:
        count = 1
    while unsolved:
        if len(array) > 1:
            if days%array[count] == 0:
                count -= 1
            else:
                days -= 1
            if count == 0:
                unsolved = False
        else:
            if days%array[0] == 0:
                count -= 1
            else:
                days -= 1
            if count == 0:
                unsolved = False

    if info[0] == 1:
        days += 1

    print('Case #'+str(case+1)+': '+str(days-1))
