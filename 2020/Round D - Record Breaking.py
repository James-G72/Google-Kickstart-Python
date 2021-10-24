# This solutio passes all cases

Cases = int(input())
for case in range(0,Cases):
    num = int(input())
    array = [int(s) for s in input().split(' ')]
    lim = 0 # The largest value seen
    recs = 0 # Number of records
    if len(array) > 1:
        if array[0] > lim:
            lim = array[0]
            if array[0] > array[1]:
                recs += 1
        for x in range(1,num-1):
            if array[x] > lim and array[x] > array[x+1]:
                recs += 1
                lim = array[x]
            elif array[x] > lim:
                lim = array[x]
        if array[-1] > lim:
            recs += 1
    else: # It is annoying that how to deal with this case is kinda ambiguous
        recs = 1

    print('Case #'+str(case+1)+': '+str(recs))
