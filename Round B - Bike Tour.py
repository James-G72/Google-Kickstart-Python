# This was the first challenge I ever tried and really struggled with how to handle the inputs
# Ultimately this is a simple problem with a couple of loops

Data = input()
Cases = Data[::2]
print(Cases)
count = 0
for i in range(1,Data[0]+1):
    peaks = 0
    for x in range(1,len(Cases[i])-1):
        if Cases[i][x] > Cases[i][x-1] and Cases[i][x] > Cases[i][x+1]:
            peaks += 1
    print('Case # '+str(i)+' '+str(peaks))
