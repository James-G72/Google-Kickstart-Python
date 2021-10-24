# This passes for all cases - not yet

Cases = int(input())
for case in range(0,Cases):
    number, max = [int(s) for s in input().split(' ')]
    withdraw = [int(s) for s in input().split(' ')]
    leave_list = ""
    leave_tally = 0
    number_list = [s for s in range(1, number+1)]
    while leave_tally < number:
        withdraw[:] = [x-max for x in withdraw]
        remove_list_1 = []
        remove_list_2 = []
        for x in range(0, len(withdraw)):
            if withdraw[x] <= 0:
                remove_list_1.append(number_list[x])
                remove_list_2.append(withdraw[x])
                leave_list += " "+str(number_list[x])
                leave_tally += 1
        for x in range(0, len(remove_list_1)):
            number_list.remove(remove_list_1[x])
            withdraw.remove(remove_list_2[x])

    print("Case #"+str(case+1)+":"+leave_list)
