# This one is just a case of handling the inputs and putting in some basic loops

Cases = range(0,int(input()))
for case in Cases:
    result = 0
    nums = input()
    nums = [int(s) for s in nums.split(' ')]
    m = nums[1]
    array = input()
    array = [int(s) for s in array.split(' ')]
    trigger = 0
    for x in array:
        if trigger:
            if x == target:
                target -= 1
            else:
                target = m
                trigger = 0
            if x == 1 and target == 0 and trigger:
                result += 1
        if x == m:
            trigger = 1
            target = m-1
    print('Case #'+str(case+1)+': '+str(result))
