# This passes S1 and TLEs for S2

Cases = int(input())
for case in range(0,Cases):
    wheels, maxim = [int(s) for s in input().split(' ')]
    initials = [int(s) for s in input().split(' ')]
    total_list = []
    for target in range(1, maxim+1):
        total = 0
        for value in initials:
            if target >= value:
                total += min(target-value, value-target+maxim)
            else:
                total += min(value-target, target-value+maxim)
        total_list.append(total)

    print("Case #"+str(case+1)+": "+str(min(total_list)))

