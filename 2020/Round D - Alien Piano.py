# Passes all test cases

Cases = int(input())
for case in range(0,Cases):
    num = int(input())
    array = [int(s) for s in input().split(' ')]
    ups = 0
    downs = 0
    breaks = 0
    for x in range(1,len(array)):
        if array[x] > array[x-1]:
            ups += 1
            downs = 0
        elif array[x] < array[x-1]:
            downs += 1
            ups = 0
        else:
            # It is equal to the next note so we don't do anything
            t = 1
        if ups > 3 or downs > 3:
            breaks += 1
            ups = downs = 0


    print('Case #'+str(case+1)+': '+str(breaks))
