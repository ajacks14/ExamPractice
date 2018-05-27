def searchneg(list):
    for x in list:
        if x < 0:
            return x
    return None


print(searchneg([1,2,3,4,5,1,-9,10]))