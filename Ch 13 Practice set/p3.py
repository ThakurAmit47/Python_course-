l = [1, 2, 3, 4, 5, 6, 10]

def five(n):
    if(n%5 == 0):
        return True
    return False
Onlyeven = filter(five, l)
print(list(Onlyeven))
#completed