try:    
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)
    print("Enter the  number bro😅")



# We can also specify the exception to catch like below:
try: 
# Code 
except ZeroDivisionError: 
# Code 
except TypeError: 
# Code 
except: 
# Code       
# All other exceptions are handled here
