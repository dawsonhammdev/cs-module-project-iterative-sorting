array = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

def bythree(array):
    for i in array:
        # if i divided by 3 the remainder is 0 then thats 
        if i%3 == 0:
            # what we want to print out
            print(i)

bythree(array)

