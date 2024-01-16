class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setAge(self, age):
        if age >= 0:
            self.__age = age

    def getAge(self):
        return self.__age
    
    def __str__(self):
        return "Name: "+self.__name+"\nAge: "+str(self.__age)

class Employee(Person):
    def __init__(self, name, age, title, rate):
        super().__init__(name, age)
        #must still set the unique attributes of employees: {title, rate}
        self.__title = title
        self.__rate = rate

    def __str__(self):
        return super().__str__() + "\ntitle: "+self.__title + " rate: $"+str(self.__rate)
#main
e1 = Employee("aaron", 29, "Instructor", 20)
print(e1)
