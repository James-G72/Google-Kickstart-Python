# This passes for all cases - not yet

Cases = int(input())
for case in range(0,Cases):
    number, max = [int(s) for s in input().split(' ')]
    withdraw = [int(s) for s in input().split(' ')]
    numbers = [x for x in range(1,number+1)]
    leave_list = []
    j = 0
    while len(numbers) > 0:
        if withdraw[j] <= max:
            leave_list.append(numbers[j])
            numbers.remove(numbers[j])
            withdraw.remove(withdraw[j])
        else:
            x = numbers[j]
            y = withdraw[j]
            numbers.remove(x)
            withdraw.remove(y)

            numbers.append(x)
            withdraw.append(y-max)
    leave_string = " ".join(map(str,leave_list))

    print("Case #"+str(case+1)+": "+leave_string)
