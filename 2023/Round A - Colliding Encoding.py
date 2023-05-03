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


alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Cases = int(input())
for case in range(0,Cases):
    mapping_arr = [int(s) for s in input().split(' ')]
    mapping_dict = {}
    for idx,letter in enumerate(alphabet):
        mapping_dict[letter] = mapping_arr[idx]

    encode = []
    collide = "NO"
    options = int(input())
    all_strings = [input().strip() for i in range(options)]
    if actual_calc(all_strings, mapping_dict):
        print('Case #'+str(case+1)+': YES')
    else:
        print('Case #'+str(case+1)+': NO')
