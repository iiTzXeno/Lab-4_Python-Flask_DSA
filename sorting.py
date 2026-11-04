class BubbleSort:
    def __init__(self, data_list):
        # Clean and store the input data
        self.original_data = [item.strip() for item in data_list if item.strip()]

    def sort_with_steps(self):
        """
        Performs bubble sort and records every state change/swap 
        so the frontend can animate it step-by-step.
        """
        arr = list(self.original_data)
        n = len(arr)
        steps = []
        
        # Capture initial state
        steps.append({
            "array": list(arr),
            "comparing": [],
            "swapped": False,
            "message": "Initial array state."
        })

        if n <= 1:
            return arr, steps

        for i in range(n):
            swapped_in_pass = False
            for j in range(0, n - i - 1):
                # Record elements currently being compared
                steps.append({
                    "array": list(arr),
                    "comparing": [j, j + 1],
                    "swapped": False,
                    "message": f"Comparing '{arr[j]}' and '{arr[j+1]}'."
                })

                # Compare elements (supports both numbers and strings alphabetically)
                val1 = arr[j]
                val2 = arr[j + 1]
                
                # Try converting to float if numeric for proper sorting comparison
                try:
                    comp1 = float(val1)
                    comp2 = float(val2)
                except ValueError:
                    comp1 = str(val1).lower()
                    comp2 = str(val2).lower()

                if comp1 > comp2:
                    # Swap elements
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped_in_pass = True
                    steps.append({
                        "array": list(arr),
                        "comparing": [j, j + 1],
                        "swapped": True,
                        "message": f"Swapped '{val2}' and '{val1}'."
                    })

            if not swapped_in_pass:
                break

        # Capture final sorted state
        steps.append({
            "array": list(arr),
            "comparing": [],
            "swapped": False,
            "message": "Sorting complete!"
        })

        return arr, steps

class SelectionSort:
    def __init__(self, data_list):
        self.original_data = [item.strip() for item in data_list if item.strip()]

    def sort_with_steps(self):
        arr = list(self.original_data)
        n = len(arr)
        steps = []
        
        steps.append({
            "array": list(arr),
            "comparing": [],
            "swapped": False,
            "message": "Initial array state."
        })

        if n <= 1:
            return arr, steps

        for i in range(n):
            min_idx = i
            steps.append({
                "array": list(arr),
                "comparing": [i],
                "swapped": False,
                "message": f"Setting current minimum position to index {i} ('{arr[i]}')."
            })

            for j in range(i + 1, n):
                steps.append({
                    "array": list(arr),
                    "comparing": [min_idx, j],
                    "swapped": False,
                    "message": f"Comparing current minimum '{arr[min_idx]}' with '{arr[j]}'."
                })

                val1 = arr[j]
                val2 = arr[min_idx]
                
                try:
                    comp1 = float(val1)
                    comp2 = float(val2)
                except ValueError:
                    comp1 = str(val1).lower()
                    comp2 = str(val2).lower()

                if comp1 < comp2:
                    min_idx = j
                    steps.append({
                        "array": list(arr),
                        "comparing": [min_idx],
                        "swapped": False,
                        "message": f"New minimum found: '{arr[min_idx]}'."
                    })

            if min_idx != i:
                swap_from = min_idx
                swap_to = i
                
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                steps.append({
                    "array": list(arr),
                    "comparing": [i, min_idx],
                    "swapped": True,
                    "swap_from": swap_from,
                    "swap_to": swap_to,
                    "message": f"Swapped minimum element into position {i}."
                })

        steps.append({
            "array": list(arr),
            "comparing": [],
            "swapped": False,
            "message": "Selection Sort complete!"
        })

        return arr, steps

class InsertionSort:
    def __init__(self, data_list):
        self.original_data = [item.strip() for item in data_list if item.strip()]

    def sort_with_steps(self):
        arr = list(self.original_data)
        n = len(arr)
        steps = []

        def parse_val(v):
            try:
                return float(v)
            except ValueError:
                return str(v).lower()

        # Initial array state
        steps.append({
            "array": list(arr),
            "phase": "static",
            "message": "Initial array state."
        })

        if n <= 1:
            return arr, steps

        # Traverse starting from index 0
        for i in range(n):
            j = i
            moved = False

            # Highlight the current key first
            steps.append({
                "array": list(arr),
                "phase": "highlight",
                "key_idx": j,
                "shift_idx": None,
                "message": f"Current key: '{arr[j]}' at index {j}."
            })

            while j > 0 and parse_val(arr[j-1]) > parse_val(arr[j]):

                # Highlight Yellow (shift) and Red (key)
                steps.append({
                    "array": list(arr),
                    "phase": "highlight",
                    "key_idx": j,
                    "shift_idx": j - 1,
                    "message": f"Highlighting: '{arr[j]}' prepares to hop over '{arr[j-1]}'."
                })

                # Swap values
                arr[j], arr[j-1] = arr[j-1], arr[j]
                moved = True

                # Animate physical jump and slide
                steps.append({
                    "array": list(arr),
                    "phase": "animate",
                    "key_idx": j - 1,
                    "shift_idx": j,
                    "message": f"'{arr[j-1]}' hops left over '{arr[j]}'."
                })

                j -= 1

        # Sorting complete
        steps.append({
            "array": list(arr),
            "phase": "static",
            "message": "Insertion Sort complete!"
        })

        return arr, steps

