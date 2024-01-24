class Stack:
    def __int__(self):
        self.__items = []
        
    def push(self, e):
        self.__items.append(e)
    
    def pop(self):

        if self.is_empty():
            raise IndexError("Index is empty")
        #to-do implement if list is empty
        return self.__items.pop()
    
    def top(self):
        return self.__items[-1]
    
    def is_empty(self):
        return len(self.__items) == 0
    
    def __len__(self):
        return len(self.__items)
    

s = Stack()
s.push(5)
s.push(3)

print(len(s))

print(s.pop())

print(s.is_empty)