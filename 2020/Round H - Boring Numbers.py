# This passes both test cases. Methedology stolen

def boring_check(num):
    digits = list(map(int, list(str(num))))
    base = 5**(len(digits)-1)
    result = (5*base-5)//(5-1)
    for poss, digit in enumerate(digits,1):
        result += (digit+1-poss%2)//2 * base
        if poss%2 != digit%2:
            break
        base //= 5
    return result

Cases = int(input())
for case in range(0,Cases):
    L,R = [int(s) for s in input().split(' ')]
    boring = boring_check(R+1) - boring_check(L)

    print("Case #"+str(case+1)+": "+str(boring))

