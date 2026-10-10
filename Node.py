# For linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove_beginning(self):
        if not self.head:
            return None

        data = self.head.data
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return data
   
    def remove_at_end(self):
        if not self.tail:
            return None
        
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
        return data

    def remove_at(self, data):
        if not self.head:
            return None
        if self.head.data == data:
            return self.remove_beginning()

        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                removed_data = current_node.next.data

                if current_node.next == self.tail:
                    self.tail = current_node
                current_node.next = current_node.next.next
                return removed_data
            
            current_node = current_node.next
        return None

    def insert_after(self, nodedata, data):
        current_node = self.head

        while current_node:
            if current_node.data == nodedata:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node

                if current_node == self.tail:
                    self.tail = new_node
                return data
            
            current_node = current_node.next
        return None

    def get_elements(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# For stack
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None


    def print_stack(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current = self.top
            print("Stack elements (top → bottom):")
            while current:
                print(current.data)
                current = current.next

# For PEMDAS Postfix Converter using Stack
class PostfixConverter:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def infix_to_postfix(self, expression):
        stack = Stack()
        output = []
        
        # Clean spaces
        expression = expression.replace(" ", "")
        
        for char in expression:
            # If operand (letter or digit), add to output
            if char.isalnum():
                output.append(char)
            # If '(', push to stack
            elif char == '(':
                stack.push(char)
            # If ')', pop until '(' is found
            elif char == ')':
                while stack.top and stack.top.data != '(':
                    output.append(stack.pop())
                if stack.top and stack.top.data == '(':
                    stack.pop()
            # If operator
            elif char in self.precedence:
                while (stack.top and stack.top.data != '(' and 
                       stack.top.data in self.precedence and 
                       self.precedence[stack.top.data] >= self.precedence[char]):
                    output.append(stack.pop())
                stack.push(char)
                
        # Pop remaining operators from stack
        while stack.top:
            if stack.top.data == '(':
                stack.pop() # Remove leftover parenthesis if any
            else:
                output.append(stack.pop())
                
        return "".join(output)

# For queue
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def get_elements(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# For deque (Double-Ended Queue)
class Deque:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, data):
        new_node = Deque(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def add_rear(self, data):
        new_node = Deque(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None
        else:
            self.rear = None
        return removed_data

    def remove_rear(self):
        if self.is_empty():
            return None
        removed_data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is not None:
            self.rear.next = None
        else:
            self.front = None
        return removed_data

    def get_elements(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return elements