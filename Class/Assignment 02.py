# Sushil Thapa
# C0919991
# Assignment 02
# 2024/02/06

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    
    def isEmpty(self):
        return self.size == 0
    
    def addFirst(self, element):
        new_node = Node(element, None, self.head)
        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node
            self.size += 1


    def addLast(self, element):
        new_node = Node(element, self.tail, None)
        if self.tail is not None:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    
    def removeFirst(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return data
    

    def removeLast(self):
        if self.isEmpty():
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return data
    
    def add(self, element, index):
        if (index < 0 or index > self.size):
            print("Invalid Index")
            return
        if index == 0:
            self.addFirst(element)
        elif index == self.size:
            self.addLast(element)
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node = Node(element, current)
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            print("Invalid Index")
            return
        if index == 0:
            return self.removeFirst()
        elif index == self.size - 1:
            return self.removeLast()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
            return current.data

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return '\n'.join(map(str, result))
    

    def __eq__(self, other):
        if self.size != other.size:
            return False
        current_self = self.head
        current_other = other.head
        while current_self is not None:
            if current_self.data != current_other.data:
                return False
            current_Self = current_self.next
            current_other = current_other.next
        return True
    
    def __add__(self, other):
        new_list = DoublyLinkedList()
        current_self = self.head
        while current_self is not None:
            new_list.addLast(current_self.next)
            current_self = current_self.next
        current_other = other.head
        while current_other is not None:
            new_list.addLast(current_other.data)
            current_other = current_other.next
        return new_list
    
    def __len__(self):
        return self.size
    



class Stack:
    def __init__(self):
        self.stk = DoublyLinkedList()
        self.size = 0 

    def isEmpty(self):
        return self.stk.isEmpty()
    
    def push(self, element):
        self.stk.addLast(element)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return None
        return self.stk.removeLast()
    
    def __str__(self):
        return f"Size: {self.size}\nTop: {self.peek()}"

    def __len__(self):
        return self.size
    
    def __add__(self, other):
        new_stack = Stack()
        new_stack.stk = self.stk + other.stk
        new_stack.size = len(new_stack.stk)
        return new_stack
    


def is_palindrome(word):
    stack = Stack()
    length = len(word)

    for i in range(length // 2):
        stack.push(word[i])

    if length % 2 != 0:
        start_index = length // 2 + 1
    else:
        start_index = length // 2

    for i in range(start_index, length):
        if word[i] != stack.pop():
            return False

    return True
        

def main():
    user_word = input("Please enter a word: ").lower()
    
    if is_palindrome(user_word):
        print(f"{user_word} is a palindrome!")
    else:
        print(f"{user_word} is not a palindrome!")

if __name__ == "__main__":
    main()

        