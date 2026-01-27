a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

if(b == 0):
    raise ZeroDivisionError("Madarchod python zero se divide nhi karti")
else:
    print(f"The division of a and b is: {a/b}")