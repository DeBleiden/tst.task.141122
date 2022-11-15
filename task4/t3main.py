
# Human class
class Human:
    def __init__(self, name, gender, position, salary):
        self.name = name
        self.gender = gender
        self.position = position
        self.salary = salary


# Person class which inherits Human class
class Person(Human):
    def __init__(self, name, gender, position, salary):
        super().__init__(name, gender, position, salary)

    def getUp(self):
        print(self.name + "(" + self.gender + ") is getting up.")

    def sit(self):
        print(self.name + "(" + self.gender + ") is going to sit on the chair.")

    def layDown(self):
        print(self.name + "(" + self.gender + ") is going to lay down.")

    def goForAWork(self):
        print(self.name + "(" + self.gender + ") is going to work as "
              + self.position + " for " + self.salary + ".")

    def logTime(self):
        print(self.name + "(" + self.gender + ") is logged up hiw work time.")


# Functions
val = Person("Reinhardt", "Male", "engineer", "750$")
val.getUp()
val.sit()
val.layDown()
val.goForAWork()
val.logTime()
