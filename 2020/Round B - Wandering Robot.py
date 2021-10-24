# A shame as I got it to work for the examples but it fails the first test case
# The logic is tricky and I gave up


num = int(input())
for run in range(1,num+1):
    Data = input()
    Data = Data.replace(" ","")
    W = int(Data[0]) # Arena width
    H = int(Data[1]) # Arena Height
    L = int(Data[2]) # Top-left column
    R = int(Data[3]) # Top-left row
    U = int(Data[4]) # Bottom-right columnn
    D = int(Data[5]) # Bottom-right row
    prob = 0
    # A few things to speed it up
    if W == U and L == 1:
        prob = 0
    elif H == D and R == 1:
        prob = 0
    else:
        gap_top = R-1
        gap_left = L-1
        gap_bottom = H-D - 1
        gap_right = W-U - 1
        if gap_bottom < 0:
            gap_bottom = 0
        if gap_right < 0:
            gap_bottom = 0
        prob_top = gap_top * 0.5**(W-1)
        prob_left = gap_left * 0.5**(H-1)
        prob_bottom = gap_bottom * 0.5**(W-1)
        prob_right = gap_right * 0.5**(H-1)
        prob = prob_left + prob_right + prob_top + prob_bottom

    print('Case #'+str(run)+': '+str(prob))
