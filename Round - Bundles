# This passes both of the example cases but the solution won't work generally
# There are issues with the way it handles the initial array as well as when there are multiple depths without a change of group

# This is going to be hard...........
# I think I'm going to try and use the alphabet to do it and make sure it works for test case 1
# Plan is to try and make a group that starts with each letter of the alphabet. That's the worst case
# Then check each group and try and make a better sub group
# Decisions can be made in an order which makes it easier but there's no way it'll work for case 2

def check(group,score,depth):
    dropped = [x[1:] for x in group if len(x) > 1]
    starts = set([x[0] for x in dropped])
    for letter in starts: # Through all starting letters
        group_2 = []
        for word in dropped:
            if word[0] == letter:
                group_2.append(word)
        if len(group_2) > 1: # If we have multiple
            depth += 1
            score = check(group_2,score,depth)
            score += depth + 1
    return score

Cases = range(0,int(input()))
for case in Cases:
    [N,K] = [int(s) for s in input().split(' ')]
    array = []
    for string in range(0,N): # Collecting inputs
        array.append(input())
    score = 0
    depth = 0
    # We treat the whole array as our first group
    score = check(array,score,depth)
    if score > 0:
        score += 1
    print('Case #'+str(case+1)+': '+str(score))
