# This passes all test cases

Cases = int(input())
for case in range(0,Cases):
    N, K, S = [int(s) for s in input().split(' ')]
    time = min(K+N,2*K-2*S+N)
    # Full logic = min((K-1)+(N+1),(K-1)+(N+1)-S+(K-S))

    print("Case #"+str(case+1)+": "+str(time))

