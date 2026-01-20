def great():
    if(a>b and a>c):
        print(f"first number is greatest: {a}")
    elif(b>a and b>c):
        print(f"Second number is greatest: {b}")
    else:
        print(f"Third number is greatest: {c}")

a = int(input("Enter 1st number: "))
b = int(input("Enter 1st number: "))
c = int(input("Enter 1st number: "))

great()