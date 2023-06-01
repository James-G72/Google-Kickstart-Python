import numpy as np

def actual_calc(string_list, La, Ra, Lb, Rb):
    """
    Applying the game logic to determine Alice's score.
    :param string_list:
    :param La: Left-most available stack for Alice
    :param Ra: Right-most available stack for Alice
    :param Lb: Left-most available stack for Bob
    :param Rb: Right-most available stack for Bob
    :return: Maximum number of pancakes for Alice
    """
    # Counting how many points are to the left and right of a given point
    count = 0
    scores_left = []
    for i in string_list:
        scores_left.append(count + i)
        count += i
    count = 0
    scores_right = []
    for i in string_list[::-1]:
        scores_right.append(count + i)
        count += i
    scores_right = scores_right[::-1]

    inversion = [x[0] > x[1] for x in zip(scores_left, scores_right)]
    first_true_left = inversion.index(next(filter(lambda i: i != False, inversion)))
    if first_true_left == 0:
        overlap = False
    else:
        overlap = scores_right[first_true_left-1] == scores_left[first_true_left-1]


    t = 1



    return score

Cases = int(input())
for case in range(0,Cases):
    stack_count = int(input())
    stack_arr = [int(s) for s in input().split(' ')]
    La, Ra, Lb, Rb = input().split(' ')

    max_pancakes = actual_calc(stack_arr, La, Ra, Lb, Rb)
    print('Case #'+str(case+1)+': '+str(max_pancakes))
