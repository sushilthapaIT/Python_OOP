class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# Node class remains the same as before

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addLast(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        else:
            removed = self.head
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return removed.data

    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is empty")
        else:
            removed = self.tail
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1
            return removed.data

    def add(self, element, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        elif index == 0:
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

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        elif index == 0:
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
        while current:
            result.append(current.data)
            current = current.next
        return ''.join(map(str, result))

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

    def __add__(self, other):
        result = DoublyLinkedList()
        current_self = self.head
        current_other = other.head
        carry = 0
        while current_self or current_other:
            if current_self:
                val_self = current_self.data
                current_self = current_self.next
            else:
                val_self = 0
            if current_other:
                val_other = current_other.data
                current_other = current_other.next
            else:
                val_other = 0
            sum_val = val_self + val_other + carry
            result.addLast(sum_val % 10)
            carry = sum_val // 10
        if carry > 0:
            result.addLast(carry)
        return result

    def __len__(self):
        return self.size


class bigNum:
    def __init__(self, value='0'):
        if value[0] == '-':
            self.sign = '-'
            value = value[1:]  # Remove the sign character
        else:
            self.sign = '+'

        integer_part, _, fractional_part = value.partition('.')
        self.integer_digits = DoublyLinkedList()
        for char in reversed(integer_part):
            self.integer_digits.addLast(int(char))
        self.fractional_digits = DoublyLinkedList()
        for char in fractional_part:
            self.fractional_digits.addLast(int(char))
        
        # If there is no fractional part, add a zero to avoid potential errors
        if not fractional_part:
            self.fractional_digits.addLast(0)

    def __str__(self):
        integer_str = str(self.integer_digits)
        fractional_str = str(self.fractional_digits)
        
        # Remove trailing ".0" if present
        if fractional_str == '0':
            return integer_str
        else:
            if self.sign == '-':
                return '-' + integer_str + '.' + fractional_str
            else:
                return integer_str + '.' + fractional_str

    def __add__(self, other):
        if self.sign == other.sign:
            result = bigNum

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addLast(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        else:
            removed = self.head
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return removed.data

    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is empty")
        else:
            removed = self.tail
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1
            return removed.data

    def add(self, element, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        elif index == 0:
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

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        elif index == 0:
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
        while current:
            result.append(current.data)
            current = current.next
        return ''.join(map(str, result))

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

    def __add__(self, other):
        result = DoublyLinkedList()
        current_self = self.head
        current_other = other.head
        carry = 0
        while current_self or current_other:
            if current_self:
                val_self = current_self.data
                current_self = current_self.next
            else:
                val_self = 0
            if current_other:
                val_other = current_other.data
                current_other = current_other.next
            else:
                val_other = 0
            sum_val = val_self + val_other + carry
            result.addLast(sum_val % 10)
            carry = sum_val // 10
        if carry > 0:
            result.addLast(carry)
        return result

    def __len__(self):
        return self.size


class bigNum:
    def __init__(self, value='0'):
        if value[0] == '-':
            self.sign = '-'
            value = value[1:]  # Remove the sign character
        else:
            self.sign = '+'

        integer_part, _, fractional_part = value.partition('.')
        self.integer_digits = DoublyLinkedList()
        for char in reversed(integer_part):
            self.integer_digits.addLast(int(char))
        self.fractional_digits = DoublyLinkedList()
        for char in fractional_part:
            self.fractional_digits.addLast(int(char))
        
        # If there is no fractional part, add a zero to avoid potential errors
        if not fractional_part:
            self.fractional_digits.addLast(0)

    def __str__(self):
        integer_str = str(self.integer_digits)
        fractional_str = str(self.fractional_digits)
        
        # Remove trailing ".0" if present
        if fractional_str == '0':
            return integer_str
        else:
            if self.sign == '-':
                return '-' + integer_str + '.' + fractional_str
            else:
                return integer_str + '.' + fractional_str

    def __eq__(self, other):
        return self.sign == other.sign and self.integer_digits == other.integer_digits and self.fractional_digits == other.fractional_digits

    def __gt__(self, other):
        if self.sign == '+' and other.sign == '-':
            return True
        elif self.sign == '-' and other.sign == '+':
            return False
        elif len(self.integer_digits) > len(other.integer_digits):
            return self.sign == '+'
        elif len(self.integer_digits) < len(other.integer_digits):
            return self.sign == '-'
        else:
            current_self = self.integer_digits.head
            current_other = other.integer_digits.head
            while current_self:
                if current_self.data > current_other.data:
                    return self.sign == '+'
                elif current_self.data < current_other.data:
                    return self.sign == '-'
                current_self = current_self.next
                current_other = current_other.next
            # Compare fractional part if integer parts are equal
            current_self = self.fractional_digits.head
            current_other = other.fractional_digits.head
            while current_self:
                if current_self.data > current_other.data:
                    return self.sign == '+'
                elif current_self.data < current_other.data:
                    return self.sign == '-'
                current_self = current_self.next
                current_other = current_other.next
        return False

    def __lt__(self, other):
        return not (self == other or self > other)

    def __add__(self, other):
        if self.sign == other.sign:
            result = bigNum()
            carry = 0
            current_self = self.integer_digits.head
            current_other = other.integer_digits.head
            while current_self or current_other:
                if current_self:
                    val_self = current_self.data
                    current_self = current_self.next
                else:
                    val_self = 0
                if current_other:
                    val_other = current_other.data
                    current_other = current_other.next
                else:
                    val_other = 0
                sum_val = val_self + val_other + carry
                result.integer_digits.addLast(sum_val % 10)
                carry = sum_val // 10
            # Handle fractional part addition
            carry_fractional = 0
            current_self = self.fractional_digits.head
            current_other = other.fractional_digits.head
            while current_self or current_other:
                if current_self:
                    val_self = current_self.data
                    current_self = current_self.next
                else:
                    val_self = 0
                if current_other:
                    val_other = current_other.data
                    current_other = current_other.next
                else:
                    val_other = 0
                sum_val = val_self + val_other + carry_fractional
                result.fractional_digits.addLast(sum_val % 10)
                carry_fractional = sum_val // 10
            if carry > 0:
                result.integer_digits.addLast(carry)
            result.sign = self.sign
            return result
        else:
            return self.__sub__(bigNum(other.sign + str(other.integer_digits)))

    def __sub__(self, other):
        if self.sign != other.sign:
            result = self.__add__(bigNum(other.sign + str(other.digits)))
            result.sign = self.sign
            return result
        elif self == other:
            return bigNum('0')
        elif self > other:
            result = bigNum()
            borrow = 0
            current_self = self.digits.head
            current_other = other.digits.head
            while current_self or current_other:
                if current_self:
                    val_self = current_self.data
                    current_self = current_self.next
                else:
                    val_self = 0
                if current_other:
                    val_other = current_other.data
                    current_other = current_other.next
                else:
                    val_other = 0
                diff_val = val_self - val_other - borrow
                if diff_val < 0:
                    diff_val += 10
                    borrow = 1
                else:
                    borrow = 0
                result.digits.addLast(diff_val)
            result.sign = self.sign
            return result
        else:
            result = other.__sub__(self)
            result.sign = '-' if self.sign == '+' else '+'
            return result

    def __mul__(self, other):
            result = bigNum()  # Initialize result to 0

            # Multiply fractional parts
            fractional_result = bigNum()  # Initialize fractional result to 0
            current_self_fractional = self.fractional_digits.head
            position_self_fractional = 0
            while current_self_fractional:
                current_other_fractional = other.fractional_digits.head
                carry = 0
                while current_other_fractional:
                    prod_val = current_self_fractional.data * current_other_fractional.data + carry
                    fractional_result.fractional_digits.addLast(prod_val % 10)
                    carry = prod_val // 10
                    current_other_fractional = current_other_fractional.next
                if carry > 0:
                    fractional_result.fractional_digits.addLast(carry)
                for _ in range(position_self_fractional):
                    fractional_result.fractional_digits.addFirst(0)  # Shift result to the left based on position
                result = result + fractional_result  # Accumulate fractional result
                fractional_result = bigNum()  # Reset fractional result for next iteration
                current_self_fractional = current_self_fractional.next
                position_self_fractional += 1

            # Multiply integer parts
            integer_result = bigNum()  # Initialize integer result to 0
            current_self_integer = self.integer_digits.head
            position_self_integer = 0
            while current_self_integer:
                current_other_integer = other.integer_digits.head
                carry = 0
                while current_other_integer:
                    prod_val = current_self_integer.data * current_other_integer.data + carry
                    integer_result.integer_digits.addLast(prod_val % 10)
                    carry = prod_val // 10
                    current_other_integer = current_other_integer.next
                if carry > 0:
                    integer_result.integer_digits.addLast(carry)
                for _ in range(position_self_integer):
                    integer_result.integer_digits.addFirst(0)  # Shift result to the left based on position
                result = result + integer_result  # Accumulate integer result
                integer_result = bigNum()  # Reset integer result for next iteration
                current_self_integer = current_self_integer.next
                position_self_integer += 1

            result.sign = '-' if self.sign != other.sign else '+'  # Determine sign of the result
            return result


    def __div__(self, other):
        result = bigNum()
        dividend = bigNum(str(self))
        divisor = bigNum(str(other))

        # Perform long division
        while dividend >= divisor:
            temp_divisor = bigNum(str(divisor))  # Make a copy of divisor
            temp_quotient = bigNum('1')  
            while dividend >= temp_divisor:
                dividend = dividend - temp_divisor
                result = result + temp_quotient
                temp_divisor = temp_divisor + temp_divisor
                temp_quotient = temp_quotient + temp_quotient

        result.sign = '-' if self.sign != other.sign else '+'
        return result

    def __len__(self):
        return len(self.integer_digits) + len(self.fractional_digits)

def main():
    with open('bigNums.txt', 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines if line.strip()]
    print("******************")
    print("BigNum Calculator")
    print("******************")
    
    result = bigNum(lines[0])
    print(f"{lines[0]} + {lines[1]} = {result}")

    operand_value = None  # Initialize operand_value outside the loop

    for i in range(2, len(lines), 2):
        operand = lines[i]
        if i + 1 < len(lines):  # Check if there are enough elements in lines
            operand_value = lines[i + 1]  # Define operand_value here for non-multiplication operations
        if operand == '+':
            operand_value = bigNum(operand_value)
            result = result + operand_value
        elif operand == '-':
            operand_value = bigNum(operand_value)
            result = result - operand_value
        elif operand == '*':
            if i + 1 < len(lines):  # Check if there are enough elements in lines
                operand_value = int(lines[i + 1])  # Convert to int directly for multiplication
            result = result * operand_value
        elif operand == '/':
            if i + 1 < len(lines):  # Check if there are enough elements in lines
                operand_value = int(operand_value)  # Convert to int directly for division
            result = result / operand_value
        print(f"{result} {operand} {operand_value} = {result}")


    print("******************")
    print("Final result")
    print("******************")
    print(result)

if __name__ == "__main__":
    main()
