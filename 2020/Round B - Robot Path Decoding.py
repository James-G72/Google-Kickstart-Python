# This took me a long time to get the logic right for
# For this reason I used functions to try and spread out the logic and make it simpler
# Pleased with the result because it is a complex problem

def LetterEffect(letter,w,h):
    if letter == 'N':
        h -= 1
    elif letter == 'S':
        h += 1
    elif letter == 'W':
        w -= 1
    elif letter == 'E':
        w += 1
    return w,h


def Unpack(string,w,h):
    letter = 0
    w = 0
    h = 0
    while letter < len(string): # Using a manipulable counter instead of a for statement
        check = True
        while check:
            if letter >= len(string):
                break
            test = string[letter]
            if test == ')':
                letter += 1
            else:
                check = False
        if test == '3':
            catch = 1
        if test.isdigit(): # If the current letter is a number
            current_string = string[letter:]
            # The challenge here is finding the outer bracket when there is more than 1
            end_brackets = [i for i,ltr in enumerate(current_string) if ltr == ')'] # Finding the index of all terminating brackets
            start_brackets = [i for i,ltr in enumerate(current_string) if ltr == '('] # Finding the index of all starting brackets
            start = 0 # This variable allows us to keep track of the state of our search
            end = 0
            searching = True
            while searching:
                if len(start_brackets) == 1 and len(end_brackets) == 1: # Then we only have 1 bracket left
                    index = end_brackets[0]
                    searching = False
                elif start >= len(start_brackets):
                    index = end_brackets[len(end_brackets)-1]
                    searching = False
                else:
                    if start_brackets[start] < end_brackets[end]:
                        start += 1
                    else:
                        end += 1
                    if start <= end:
                        index = end_brackets[end-1]
                        searching = False
            if letter+2 == letter+index-1: # If they're the same then the syntax doesn't work
                w_change,h_change = Unpack(string[letter+2],w,h) # We unpack the new inside of this bracket
            else:
                w_change,h_change = Unpack(string[letter+2:letter+index],w,h)  # We unpack the new inside of this bracket
            w += w_change*int(test) # We effect the multiplication on the changes
            h += h_change*int(test)
            letter += index+1 # We can now look beyond this function
        else:
            w,h = LetterEffect(test,w,h) # Otherwise we assess the effect of this letter. This could be done here
            letter += 1
    return w,h

t = int(input())
count = 0
for i in range(1, t + 1):
    string = input()
    w = 1  # Starting square
    h = 1
    w_change,h_change = Unpack(string,w,h) # This version of Unpack we don't use the multiplication system as it is for the final answer
    w += w_change # We effect the multiplication is 1
    h += h_change
    if w < 0:
        w = w%(1*10**9)
    elif w > (10**9):
        w = w%(1*10**9)
    elif w == 0:
        w = (10**9)
    if h < 0:
        h = h%(1*10**9)
    elif h > (10**9):
        h = h%(1*10**9)
    elif h == 0:
        h = (10**9)
    count += 1
    print('Case #'+str(i)+': '+str(w)+' '+str(h))
