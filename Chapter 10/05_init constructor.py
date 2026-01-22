#Example 
class Employee:
    language = "python" #class attributes
    salary = 30000

    def __init__(self): #ye function automatcally hota hai or ise dunder method bhi kehte hai
        print("Aman is idiot")

    def getInfo(self): #self call karna padega warna error aega
        print(f"The language is {self.language} and salary {self.salary}")

Amit = Employee()
Amit.language = "Java" #Output java aega, because instance(object) attributes over write kr deti hai class attributes pe
print(Amit.language, Amit.salary)

Amit.getInfo()
Amit = Employee()


################################################################################

#Example 
class Employee:
    language = "python" #class attributes
    salary = 30000

    def __init__(self, name, language, salary): #ye function automatcally hota hai or ise dunder method bhi kehte hai
        self.name = name
        self.language = language
        self.salary = salary
        print("Aman is idiot")


Amit = Employee("Amit", "Javascript", 40000)
print(Amit.name, Amit.language, Amit.salary)

# ek sath bohut sari cheez update kr sakte hai