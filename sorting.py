import re

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

class MergeSort:
    """Merge Sort data structure and step-by-step visualization generator."""

    def __init__(self):
        self.steps = []

    @staticmethod
    def parse_input(raw_data):
        """Parse comma- or space-separated numbers or strings into a clean list."""
        tokens = [t.strip() for t in re.split(r'[,\s]+', raw_data.strip()) if t.strip()]
        if not tokens:
            return []

        # Check if all tokens are numeric
        parsed_nums = []
        all_numeric = True
        for token in tokens:
            try:
                num = float(token)
                parsed_nums.append(int(num) if num.is_integer() else num)
            except ValueError:
                all_numeric = False
                break

        return parsed_nums if all_numeric else tokens

    @staticmethod
    def _compare_key(val):
        """Return a comparable key supporting numbers, strings, or mixed inputs."""
        if isinstance(val, (int, float)):
            return (0, float(val))
        return (1, str(val).lower())

    def sort(self, data):
        """Sort a copy of data using Merge Sort and return (sorted_list, animation_steps)."""
        arr = list(data)
        self.steps = []

        if not arr:
            return [], []

        self.steps.append({
            "array": list(arr),
            "phase": "initial",
            "message": f"Initial array: [{', '.join(map(str, arr))}]",
            "left_range": None,
            "right_range": None,
            "split_idx": None,
            "compare_indices": [],
            "placed_idx": None,
            "merged_indices": [],
            "floating_left": [],
            "floating_right": [],
            "sorted_indices": []
        })

        if len(arr) > 1:
            self._merge_sort_recursive(arr, 0, len(arr) - 1)

        self.steps.append({
            "array": list(arr),
            "phase": "done",
            "message": f"Merge Sort complete! Final sorted array: [{', '.join(map(str, arr))}]",
            "left_range": None,
            "right_range": None,
            "split_idx": None,
            "compare_indices": [],
            "placed_idx": None,
            "merged_indices": [],
            "floating_left": [],
            "floating_right": [],
            "sorted_indices": list(range(len(arr)))
        })

        return arr, self.steps

    def _merge_sort_recursive(self, arr, left, right):
        """Recursively divide the array into halves and merge them in sorted order."""
        if left >= right:
            return

        mid = (left + right) // 2
        left_slice = arr[left : mid + 1]
        right_slice = arr[mid + 1 : right + 1]

        # Record the Divide (Split) step
        self.steps.append({
            "array": list(arr),
            "phase": "split",
            "message": f"Divide: Splitting [{', '.join(map(str, arr[left:right + 1]))}] into Left [{', '.join(map(str, left_slice))}] and Right [{', '.join(map(str, right_slice))}]",
            "left_range": [left, mid],
            "right_range": [mid + 1, right],
            "split_idx": mid,
            "compare_indices": [],
            "placed_idx": None,
            "merged_indices": [],
            "floating_left": list(range(left, mid + 1)),
            "floating_right": list(range(mid + 1, right + 1)),
            "sorted_indices": []
        })

        # Recursively sort left and right halves
        self._merge_sort_recursive(arr, left, mid)
        self._merge_sort_recursive(arr, mid + 1, right)

        # Merge the two sorted halves
        self._merge(arr, left, mid, right)

    def _merge(self, arr, left, mid, right):
        """Merge two sorted subarrays arr[left..mid] and arr[mid+1..right] with step tracking."""
        left_part = arr[left : mid + 1]
        right_part = arr[mid + 1 : right + 1]

        i = 0
        j = 0
        k = left
        merged_so_far = []

        while i < len(left_part) and j < len(right_part):
            rem_left = left_part[i:]
            rem_right = right_part[j:]
            arr[left : right + 1] = merged_so_far + rem_left + rem_right

            left_curr_idx = k
            right_curr_idx = k + len(rem_left)
            floating_left = list(range(k, k + len(rem_left)))
            floating_right = list(range(k + len(rem_left), right + 1))

            # Step 1: Compare the front elements of the left and right subarrays
            self.steps.append({
                "array": list(arr),
                "phase": "compare",
                "message": f"Comparing Left '{left_part[i]}' and Right '{right_part[j]}' to merge into position {k + 1}",
                "left_range": [left, mid],
                "right_range": [mid + 1, right],
                "split_idx": right_curr_idx - 1,
                "compare_indices": [left_curr_idx, right_curr_idx],
                "placed_idx": None,
                "merged_indices": list(range(left, k)),
                "floating_left": floating_left,
                "floating_right": floating_right,
                "sorted_indices": []
            })

            # Choose smaller element (<= preserves stability)
            if self._compare_key(left_part[i]) <= self._compare_key(right_part[j]):
                chosen = left_part[i]
                i += 1
            else:
                chosen = right_part[j]
                j += 1

            merged_so_far.append(chosen)
            rem_left = left_part[i:]
            rem_right = right_part[j:]
            arr[left : right + 1] = merged_so_far + rem_left + rem_right

            new_floating_left = list(range(k + 1, k + 1 + len(rem_left)))
            new_floating_right = list(range(k + 1 + len(rem_left), right + 1))

            # Step 2: Drop the chosen element into its merged slot
            self.steps.append({
                "array": list(arr),
                "phase": "merge",
                "message": f"Merging '{chosen}' down into sorted position {k + 1}",
                "left_range": [left, mid],
                "right_range": [mid + 1, right],
                "split_idx": (k + len(rem_left)) if (rem_left and rem_right) else None,
                "compare_indices": [],
                "placed_idx": k,
                "merged_indices": list(range(left, k + 1)),
                "floating_left": new_floating_left,
                "floating_right": new_floating_right,
                "sorted_indices": []
            })
            k += 1

        # Drop any remaining elements from the left subarray
        while i < len(left_part):
            chosen = left_part[i]
            i += 1
            merged_so_far.append(chosen)
            rem_left = left_part[i:]
            arr[left : right + 1] = merged_so_far + rem_left

            self.steps.append({
                "array": list(arr),
                "phase": "merge",
                "message": f"Merging remaining left element '{chosen}' into position {k + 1}",
                "left_range": [left, mid],
                "right_range": [mid + 1, right],
                "split_idx": None,
                "compare_indices": [],
                "placed_idx": k,
                "merged_indices": list(range(left, k + 1)),
                "floating_left": list(range(k + 1, right + 1)),
                "floating_right": [],
                "sorted_indices": []
            })
            k += 1

        # Drop any remaining elements from the right subarray
        while j < len(right_part):
            chosen = right_part[j]
            j += 1
            merged_so_far.append(chosen)
            rem_right = right_part[j:]
            arr[left : right + 1] = merged_so_far + rem_right

            self.steps.append({
                "array": list(arr),
                "phase": "merge",
                "message": f"Merging remaining right element '{chosen}' into position {k + 1}",
                "left_range": [left, mid],
                "right_range": [mid + 1, right],
                "split_idx": None,
                "compare_indices": [],
                "placed_idx": k,
                "merged_indices": list(range(left, k + 1)),
                "floating_left": [],
                "floating_right": list(range(k + 1, right + 1)),
                "sorted_indices": []
            })
            k += 1

class QuickSort:
    """Quick Sort (First-Element Pivot) data structure and step-by-step visualization generator."""

    def __init__(self):
        self.steps = []
        self.fixed_sorted = set()

    @staticmethod
    def parse_input(raw_data):
        """Parse comma- or space-separated numbers or strings into a clean list."""
        tokens = [t.strip() for t in re.split(r'[,\s]+', raw_data.strip()) if t.strip()]
        if not tokens:
            return []

        parsed_nums = []
        all_numeric = True
        for token in tokens:
            try:
                num = float(token)
                parsed_nums.append(int(num) if num.is_integer() else num)
            except ValueError:
                all_numeric = False
                break

        return parsed_nums if all_numeric else tokens

    @staticmethod
    def _compare_key(val):
        """Return a comparable key supporting numbers, strings, or mixed inputs."""
        if isinstance(val, (int, float)):
            return (0, float(val))
        return (1, str(val).lower())

    def _record_step(
        self,
        arr,
        phase,
        message,
        partition_range=None,
        pivot_idx=None,
        store_idx=None,
        scan_idx=None,
        compare_indices=None,
        swap_indices=None,
        less_than_indices=None,
        greater_than_indices=None,
    ):
        self.steps.append({
            "array": list(arr),
            "phase": phase,
            "message": message,
            "partition_range": partition_range,
            "pivot_idx": pivot_idx,
            "store_idx": store_idx,
            "scan_idx": scan_idx,
            "compare_indices": compare_indices or [],
            "swap_indices": swap_indices or [],
            "less_than_indices": less_than_indices or [],
            "greater_than_indices": greater_than_indices or [],
            "sorted_indices": sorted(self.fixed_sorted),
        })

    def sort(self, data):
        """Sort a copy of data using Quick Sort and return (sorted_list, animation_steps)."""
        arr = list(data)
        self.steps = []
        self.fixed_sorted = set()

        if not arr:
            return [], []

        self._record_step(
            arr=arr,
            phase="initial",
            message=f"Initial array: [{', '.join(map(str, arr))}]",
        )

        if len(arr) > 1:
            self._quick_sort_recursive(arr, 0, len(arr) - 1)
        else:
            self.fixed_sorted.add(0)

        self.fixed_sorted = set(range(len(arr)))
        self._record_step(
            arr=arr,
            phase="done",
            message=f"Quick Sort complete! Final sorted array: [{', '.join(map(str, arr))}]",
        )

        return arr, self.steps

    def _quick_sort_recursive(self, arr, low, high):
        """Recursively partition subarrays around the first-element pivot and sort both sides."""
        if low > high:
            return

        if low == high:
            self.fixed_sorted.add(low)
            self._record_step(
                arr=arr,
                phase="single_lock",
                message=f"Single element '{arr[low]}' at index {low} is locked in sorted position",
                partition_range=[low, high],
            )
            return

        pivot_final_idx = self._partition(arr, low, high)

        self._quick_sort_recursive(arr, low, pivot_final_idx - 1)
        self._quick_sort_recursive(arr, pivot_final_idx + 1, high)

    def _partition(self, arr, low, high):
        """Partition arr[low..high] using the first element (low) as pivot."""
        pivot_val = arr[low]
        i = low + 1

        # Step 1: Announce first-index pivot selection
        self._record_step(
            arr=arr,
            phase="pivot",
            message=f"Partition [{low}..{high}]: Selected '{pivot_val}' at index {low} as Pivot",
            partition_range=[low, high],
            pivot_idx=low,
            store_idx=i,
        )

        # Step 2: Scan elements from low + 1 to high
        for j in range(low + 1, high + 1):
            self._record_step(
                arr=arr,
                phase="compare",
                message=f"Comparing '{arr[j]}' (index {j}) with Pivot '{pivot_val}'",
                partition_range=[low, high],
                pivot_idx=low,
                store_idx=i,
                scan_idx=j,
                compare_indices=[low, j],
                less_than_indices=list(range(low + 1, i)),
                greater_than_indices=list(range(i, j)),
            )

            if self._compare_key(arr[j]) <= self._compare_key(pivot_val):
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    self._record_step(
                        arr=arr,
                        phase="swap",
                        message=f"'{arr[i]}' <= Pivot '{pivot_val}': Swapping index {j} into left partition (index {i})",
                        partition_range=[low, high],
                        pivot_idx=low,
                        store_idx=i,
                        scan_idx=j,
                        swap_indices=[i, j],
                        less_than_indices=list(range(low + 1, i + 1)),
                        greater_than_indices=list(range(i + 1, j + 1)),
                    )
                else:
                    self._record_step(
                        arr=arr,
                        phase="keep",
                        message=f"'{arr[i]}' <= Pivot '{pivot_val}': Keeping in left partition (index {i})",
                        partition_range=[low, high],
                        pivot_idx=low,
                        store_idx=i,
                        scan_idx=j,
                        less_than_indices=list(range(low + 1, i + 1)),
                        greater_than_indices=[],
                    )
                i += 1

        # Step 3: Place pivot from low into its final sorted index (i - 1)
        pivot_final_idx = i - 1
        if pivot_final_idx != low:
            arr[low], arr[pivot_final_idx] = arr[pivot_final_idx], arr[low]
            self.fixed_sorted.add(pivot_final_idx)
            self._record_step(
                arr=arr,
                phase="pivot_swap",
                message=f"Placing Pivot '{arr[pivot_final_idx]}' into its final sorted position (index {pivot_final_idx})",
                partition_range=[low, high],
                pivot_idx=pivot_final_idx,
                store_idx=pivot_final_idx,
                swap_indices=[low, pivot_final_idx],
                less_than_indices=list(range(low, pivot_final_idx)),
                greater_than_indices=list(range(pivot_final_idx + 1, high + 1)),
            )
        else:
            self.fixed_sorted.add(low)
            self._record_step(
                arr=arr,
                phase="pivot_lock",
                message=f"Pivot '{arr[low]}' is already in its final sorted position (index {low})",
                partition_range=[low, high],
                pivot_idx=low,
                store_idx=low,
                less_than_indices=[],
                greater_than_indices=list(range(low + 1, high + 1)),
            )

        return pivot_final_idx