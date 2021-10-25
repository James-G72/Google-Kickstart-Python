# This passes for all cases

def list_build(iter, array, size):
    list = []
    row = max(0, size-iter-1)
    if size-iter-1 < 0:
        col = abs(size-iter-1)
    else:
        col = 0
    iter = min(iter,size-col-1)
    for num in range(0, iter+1):
        list.append(array[row][col])
        row += 1
        col += 1
    return list

Cases = int(input())
for case in range(0,Cases):
    size = int(input())
    array = []
    for x in range(0, size):
        array.append([int(s) for s in input().split(' ')])
    max_coins = 0
    for x in range(0, size*2-1):
        value = sum(list_build(x, array, size))
        if value > max_coins:
            max_coins = value

    print("Case #"+str(case+1)+": "+str(max_coins))

