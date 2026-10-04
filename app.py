from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works/touppercase', methods=['GET', 'POST'])
def toUpperCase():
    result = None
    error = None
    if request.method == 'POST':
        try:
            input_string = request.form.get('inputString', '')
            if not input_string.strip():
                raise ValueError("Input string cannot be empty.")
            result = input_string.upper()
        except ValueError as e:
            error = str(e)
    return render_template('touppercase.html', result=result, error=error)

@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    error = None
    if request.method == 'POST':
        try:
            radius_str = request.form.get('radius', '').strip()
            if not radius_str:
                raise ValueError("Radius cannot be empty.")
            
            radius = float(radius_str)
            if radius <= 0:
                raise ValueError("Radius must be a positive number.")
                
            result = radius * 3.14 * radius
        except ValueError as e:
            error = str(e)
            
    return render_template('circle.html', result=result, error=error)

# @app.route('/areaOfcirle', methods=['GET', 'POST'])
# def areaOfcirle():
#     result = None
#     name=request.get('name','')
#     print(name)
#     if request.method == 'POST':
#         input_string = request.form.get('inputradius', '')
#         result = int(input_string) * int(input_string) * 3.14
#     return render_template('areaCircle.html', result=result)


@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None
    error = None
    if request.method == 'POST':
        try:
            # If user inputs letters, float() will naturally trigger a ValueError
            base = float(request.form.get('base', ''))
            height = float(request.form.get('height', ''))
            
            result = 0.5 * base * height
        except ValueError:
            error = "Invalid input! Please enter valid numeric values only."
            
    return render_template('triangle.html', result=result, error=error)

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

my_linked_list = LinkedList()

@app.route('/works/LinkedList', methods=['GET', 'POST'])
def linked_list_page():
    message = None
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'insert_beginning':
            val = request.form.get('basic_value', '').strip()
            if val:
                my_linked_list.insert_at_beginning(val)
                message = f"Inserted '{val}' at the beginning."
            else:
                message = "Please provide a value."

        elif action == 'insert_end':
            val = request.form.get('basic_value', '').strip()
            if val:
                my_linked_list.insert_at_end(val)
                message = f"Inserted '{val}' at the end."
            else:
                message = "Please provide a value."

        elif action == 'search':
            val = request.form.get('basic_value', '').strip()
            if val:
                found = my_linked_list.search(val)
                message = f"Search for '{val}': {'Found in list' if found else 'Not found'}"
            else:
                message = "Please provide a value to search."

        elif action == 'remove_at':
            val = request.form.get('remove_value', '').strip()
            if val:
                removed = my_linked_list.remove_at(val)
                message = f"Removed node with data: {removed}" if removed is not None else f"Node '{val}' not found."
            else:
                message = "Please provide a value to remove."

        elif action == 'insert_after':
            target = request.form.get('target', '').strip()
            new_val = request.form.get('insert_value', '').strip()
            if target and new_val:
                res = my_linked_list.insert_after(target, new_val)
                message = f"Inserted '{new_val}' after '{target}'." if res is not None else f"Target node '{target}' not found."
            else:
                message = "Provide both target node and new value."

        elif action == 'remove_beginning':
            removed = my_linked_list.remove_beginning()
            message = f"Removed beginning node: {removed}" if removed is not None else "List is already empty."

        elif action == 'remove_end':
            removed = my_linked_list.remove_at_end()
            message = f"Removed end node: {removed}" if removed is not None else "List is already empty."

    elements = my_linked_list.get_elements()
    return render_template('linkedlist.html', elements=elements, message=message)



@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/works')
def works():
    return render_template('works.html')

if __name__ == "__main__":
    app.run(debug=True)
