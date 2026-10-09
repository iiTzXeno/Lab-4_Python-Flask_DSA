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