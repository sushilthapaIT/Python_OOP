class Insect:
    def __init__(self, name, type, hive, age):
        self.__name = name
        self.__type = type
        self.__hive = hive
        self.age = age

    def getName(self):
        return self.__name
    
    def getHive(self):
        return self.__hive
    
i1 = Insect("Butterfly", "ins", "yes", 18)

#need to return the and print with function for __ private attribute they cant be acced with out returning from a function.
print(i1.getName(), i1.age)