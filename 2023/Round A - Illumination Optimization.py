import numpy as np

def actual_calc(string_list, map_dict):
    """
    A function that returns true for collisions and false for no collisions
    :param string_list: input of all strings to compare in a list
    :return: True or False
    """
    comp_list = set()
    for string in string_list:
        cipher = ''.join(str(map_dict[letter]) for letter in string)
        if cipher in comp_list:
            return True
        comp_list.add(cipher)
    return False


Cases = int(input())
for case in range(0,Cases):
    length,radius,quantity = input().split()
    locations = [int(x) for x in input().split()]

    gaps = np.diff(locations)
    if max(gaps) <= radius:
        full_coverage = False
        idx = 0
        while not full_coverage:


    else:
        print('Case #'+str(case+1)+': IMPOSSIBLE')