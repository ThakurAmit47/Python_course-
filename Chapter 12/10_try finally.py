def main():
    try:    
        a = int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        print("Enter the  number bro😅")
        return

    finally:
        print("final is excution")

main()

#########-Finally ka main use function me hota hai tab return lagne ke print kam nhi karta. to finaly lagake run karaya jata hai 