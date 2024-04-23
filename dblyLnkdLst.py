# Sushil Thapa
# C0919991
# Test 01

# Node class for creating nodes
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# DoublyLinkedList class for creating a doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Checking if the linked list is empty
    def isEmpty(self):
        return self.head == None and self.tail == None

    # Adding an element to the beginning of the linked list
    def addFirst(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    # Adding an element to the end of the linked list
    def addLast(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    # Removing the first element from the linked list
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return data

    # Removing the last element from the linked list
    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is empty")
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return data

    # Adding an element at a specified index
    def add(self, element, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.addFirst(element)
        elif index == self.size:
            self.addLast(element)
        else:
            new_node = Node(element)
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1

    # Removing an element from a specified index
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.removeFirst()
        elif index == self.size - 1:
            return self.removeLast()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            data = current.data
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
            return data

    # Converting the linked list to a string representation
    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next
        return result

    # Checking if two linked lists are equal
    def __eq__(self, other):
        if self.size != other.size:
            return False
        current_self = self.head
        current_other = other.head
        while current_self:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True

    # Concatenating two linked lists
    def __add__(self, other):
        current_other = other.head
        self.tail.next = other.head
        other.head.prev = self.tail
        self.tail = other.tail

    # Getting the length of the linked list
    def __len__(self):
        return self.size
