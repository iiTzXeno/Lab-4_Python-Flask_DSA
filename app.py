from flask import Flask, render_template, request
from nodes import Node, BinaryNode, LinkedList, Stack, PostfixConverter, Queue, Deque, BinaryTree
from sorting import BubbleSort, SelectionSort, InsertionSort, MergeSort, QuickSort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/works')
def works():
    return render_template('works.html')

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

my_linked_list = LinkedList()
my_stack = Stack()
my_queue = Queue()
my_deque = Deque()
my_postfix = PostfixConverter()

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
    return render_template('LinkedList.html', elements=elements, message=message)

@app.route('/works/stack', methods=['GET', 'POST'])
def stack_page():
    message = "Ready"
    single_value = None
    print_text = None
    print_elements = []  
    
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'push':
            val = request.form.get('value', '').strip()
            if val:
                my_stack.push(val)
                message = f"Pushed '{val}' onto the stack."
            else:
                message = "Please provide a value."

        elif action == 'pop':
            popped = my_stack.pop()
            if popped is not None:
                message = "Popped value successfully."
                single_value = popped
            else:
                message = "Stack is empty."

        elif action == 'peek':
            top_val = my_stack.peek()
            if top_val is not None:
                message = "Peeked top element."
                single_value = top_val
            else:
                message = "Stack is empty."

        elif action == 'print':
            current = my_stack.top
            temp_list = []
            while current:
                temp_list.append(str(current.data))
                current = current.next
            
            if temp_list:
                # Text format output
                print_text = "Stack elements (top → bottom):\n" + "\n".join(temp_list)
                # Visual box elements
                print_elements = temp_list
                message = "Stack printed successfully."
            else:
                print_text = "Stack is empty"
                message = "Stack is empty."

    return render_template('stack.html', message=message, single_value=single_value, print_text=print_text, print_elements=print_elements)

@app.route('/works/postfix', methods=['GET', 'POST'])
def postfix_page():
    result = None
    error = None
    if request.method == 'POST':
        try:
            expr = request.form.get('expression', '').strip()
            if not expr:
                raise ValueError("Expression cannot be empty.")
            result = my_postfix.infix_to_postfix(expr)
        except ValueError as e:
            error = str(e)
    return render_template('postfix.html', result=result, error=error)

@app.route('/works/queue', methods=['GET', 'POST'])
def queue_page():
    message = None
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'enqueue':
            val = request.form.get('value', '').strip()
            if val:
                my_queue.enqueue(val)
                message = f"Enqueued '{val}' to the queue."
            else:
                message = "Please provide a value."

        elif action == 'dequeue':
            dequeued = my_queue.dequeue()
            message = f"Dequeued value: {dequeued}" if dequeued is not None else "Queue is empty."

    elements = my_queue.get_elements() if hasattr(my_queue, 'get_elements') else []
    return render_template('queue.html', elements=elements, message=message)


@app.route('/works/deque', methods=['GET', 'POST'])
def deque_page():
    message = None
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add_front':
            val = request.form.get('value', '').strip()
            if val:
                my_deque.add_front(val)
                message = f"Added '{val}' to front."
            else:
                message = "Please provide a value."

        elif action == 'add_rear':
            val = request.form.get('value', '').strip()
            if val:
                my_deque.add_rear(val)
                message = f"Added '{val}' to rear."
            else:
                message = "Please provide a value."

        elif action == 'remove_front':
            removed = my_deque.remove_front()
            message = f"Removed from front: {removed}" if removed is not None else "Deque is empty."

        elif action == 'remove_rear':
            removed = my_deque.remove_rear()
            message = f"Removed from rear: {removed}" if removed is not None else "Deque is empty."

    elements = my_deque.get_elements() if hasattr(my_deque, 'get_elements') else []
    return render_template('deque.html', elements=elements, message=message)

# For Binary Tree
global_tree = BinaryTree()

@app.route('/works/binarytree', methods=['GET', 'POST'])
def binary_tree_page():
    global global_tree
    message = "Tree is currently empty. Set a root node to begin."
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'reset':
            global_tree = BinaryTree()
            message = "Tree has been reset (emptied)."
            
        elif action == 'create_root':
            root_val = request.form.get('root_value', '').strip()
            if root_val:
                global_tree = BinaryTree(root_val)
                message = f"Root node '{root_val}' created successfully."
            else:
                message = "Please provide a valid root value."
            
        elif action == 'insert':
            parent_val = request.form.get('parent_value', '').strip()
            child_val = request.form.get('child_value', '').strip()
            direction = request.form.get('direction', 'left')
            
            if not global_tree.root:
                message = "Error: Tree has no root! Create a root node first."
            elif parent_val and child_val:
                parent_node = global_tree.search(global_tree.root, parent_val)
                if parent_node:
                    if direction == 'left':
                        global_tree.insert_left(parent_node, child_val)
                    else:
                        global_tree.insert_right(parent_node, child_val)
                    message = f"Inserted '{child_val}' as {direction} child of '{parent_val}'."
                else:
                    message = f"Parent node '{parent_val}' not found in the tree."
            else:
                message = "Please provide both parent and child values."

        elif action == 'delete':
            delete_val = request.form.get('delete_value', '').strip()
            if not global_tree.root:
                message = "Error: Tree is already empty."
            elif delete_val:
                if global_tree.search(global_tree.root, delete_val):
                    global_tree.root = global_tree.delete_node(global_tree.root, delete_val)
                    message = f"Node '{delete_val}' deleted successfully."
                else:
                    message = f"Node '{delete_val}' not found in the tree."
            else:
                message = "Please provide a value to delete."

    # Compute Traversals
    preorder = global_tree.preorder_traversal(global_tree.root, "").strip() if global_tree.root else ""
    inorder = global_tree.inorder_traversal(global_tree.root, "").strip() if global_tree.root else ""
    postorder = global_tree.postorder_traversal(global_tree.root, "").strip() if global_tree.root else ""
    
    tree_json = global_tree.to_dict(global_tree.root) if global_tree.root else None

    return render_template(
        'binary_tree.html',
        tree_data=tree_json,
        preorder=preorder,
        inorder=inorder,
        postorder=postorder,
        message=message
    )

# For Sorting Algorithm 
@app.route('/works/bubblesort', methods=['GET', 'POST'])
def bubble_sort_page():
    steps_json = []
    sorted_result = []
    user_input = ""
    
    if request.method == 'POST':
        user_input = request.form.get('input_data', '').strip()
        if user_input:
            # Split input string by commas or spaces (e.g., "5, 2, 9, 1" or "banana, apple, cherry")
            if ',' in user_input:
                raw_list = user_input.split(',')
            else:
                raw_list = user_input.split()
                
            sorter = BubbleSort(raw_list)
            sorted_result, steps_json = sorter.sort_with_steps()
            
    return render_template(
        'bubble_sort.html', 
        steps=steps_json, 
        sorted_result=sorted_result, 
        user_input=user_input
    )

@app.route('/works/selectionsort', methods=['GET', 'POST'])
def selection_sort_page():
    steps_json = []
    sorted_result = []
    user_input = ""
    
    if request.method == 'POST':
        user_input = request.form.get('input_data', '').strip()
        if user_input:
            if ',' in user_input:
                raw_list = user_input.split(',')
            else:
                raw_list = user_input.split()
                
            sort_obj = SelectionSort(raw_list)
            sorted_result, steps_json = sort_obj.sort_with_steps()
            
    return render_template(
        'selection_sort.html', 
        steps=steps_json, 
        sorted_result=sorted_result, 
        user_input=user_input
    )

@app.route('/works/insertionsort', methods=['GET', 'POST'])
def insertion_sort_page():
    steps_json = []
    sorted_result = []
    user_input = ""
    
    if request.method == 'POST':
        user_input = request.form.get('input_data', '').strip()
        if user_input:
            if ',' in user_input:
                raw_list = user_input.split(',')
            else:
                raw_list = user_input.split()
                
            sort_obj = InsertionSort(raw_list)
            sorted_result, steps_json = sort_obj.sort_with_steps()
            
    return render_template(
        'insertion_sort.html', 
        steps=steps_json, 
        sorted_result=sorted_result, 
        user_input=user_input
    )

@app.route('/works/mergesort', methods=['GET', 'POST'])
def merge_sort_page():
    steps = []
    sorted_result = None
    user_input = ""

    if request.method == 'POST':
        user_input = request.form.get('input_data', '').strip()
        sorter = MergeSort()
        parsed_data = sorter.parse_input(user_input)

        if parsed_data:
            sorted_result, steps = sorter.sort(parsed_data)

    return render_template(
        'merge_sort.html',
        steps=steps,
        sorted_result=sorted_result,
        user_input=user_input
    )

@app.route('/works/quicksort', methods=['GET', 'POST'])
def quick_sort_page():
    steps = []
    sorted_result = None
    user_input = ""

    if request.method == 'POST':
        user_input = request.form.get('input_data', '').strip()
        sorter = QuickSort()
        parsed_data = sorter.parse_input(user_input)

        if parsed_data:
            sorted_result, steps = sorter.sort(parsed_data)

    return render_template(
        'quick_sort.html',
        steps=steps,
        sorted_result=sorted_result,
        user_input=user_input
    )

if __name__ == "__main__":
    app.run(debug=True)
