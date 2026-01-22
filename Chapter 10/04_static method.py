#Example 
class Employee:
    language = "python" #class attributes
    salary = 30000

    @staticmethod  #self call na karna ho to static method lagti hai. but iske baad instance attributes print nhi hoga sirf class attributes tak hi access rahega
    def getInfo(): 
        print("Good Morning")

Amit = Employee()
Amit.language = "Java" #Output java aega, because instance(object) attributes over write kr deti hai class attributes pe
print(Amit.language, Amit.salary)

Amit.getInfo()