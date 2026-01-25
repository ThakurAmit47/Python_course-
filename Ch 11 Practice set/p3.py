class employee:
    salary = 50000
    increment = 30

    @property
    def SalaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment/100)

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, salary):
        self.increment = (salary/self.salary -1)*100
a = employee()
print(a.SalaryAfterIncrement, a.increment)