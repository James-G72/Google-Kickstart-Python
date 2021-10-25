# This passes for all cases

Cases = int(input())
for case in range(0,Cases):
    book = input()
    kick_count = 0
    frag_count = 0
    for index in range(0,len(book)-4):
        if book[index:index+4] == "KICK":
            kick_count += 1
        if book[index:index+5] == "START":
            frag_count += kick_count

    print("Case #"+str(case+1)+": "+str(frag_count))

