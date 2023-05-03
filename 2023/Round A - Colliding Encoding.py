alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Cases = int(input())
for case in range(0,Cases):
    mapping_arr = [int(s) for s in input().split(' ')]
    mapping_dict = {}
    for idx,letter in enumerate(alphabet):
        mapping_dict[letter] = mapping_arr[idx]

    encode = []
    collide = "NO"
    for tests in range(0,int(input())):
        check_set = ""
        for letter in input():
            check_set += str(mapping_dict[letter])
        encode.append(check_set)
    if len(encode) != len(set(encode)):
        collide = "YES"

    print('Case #'+str(case+1)+': '+collide)
