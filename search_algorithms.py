import math
import timeit


class SearchAlgorithms:
    # --- Linear Search ---
    @staticmethod
    def linear_search(arr, target):
        for i, element in enumerate(arr):
            if element == target:
                return i

        return -1

    @staticmethod
    def linear_search_wrapper(func, *args, **kwargs):
        return func(*args, **kwargs)

    # --- Binary Search ---
    @staticmethod
    def binary_search(array, target):
        low, high = 0, len(array) - 1

        while low <= high:
            mid = (low + high) // 2

            if array[mid] == target:
                return mid
            elif array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    @staticmethod
    def binary_search_wrapper1(array, target):
        return SearchAlgorithms.binary_search(arr, target)

    @staticmethod
    def binary_search_wrapper(func, *args, **kwargs):
        return func(*args, **kwargs)

    # --- Exponential Search ---
    @staticmethod
    def exponential_binary_search(arr, target, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    @staticmethod
    def exponential_search(arr, target):
        if arr[0] == target:
            return 0
        i = 1
        n = len(arr)
        while i < n and arr[i] <= target:
            i *= 2
        return SearchAlgorithms.exponential_binary_search(arr, target, i // 2, min(i, n) - 1)

    @staticmethod
    def exponential_search_wrapper(func, *args, **kwargs):
        return func(*args, **kwargs)

    # --- Interpolation Search ---
    @staticmethod
    def interpolation_search(arr, target):
        low, high = 0, len(arr) - 1

        while low <= high and target >= arr[low] and target <= arr[high]:
            if low == high:
                if arr[low] == target:
                    return low
                return -1

            pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1

        return -1

    @staticmethod
    def interpolation_search_wrapper(func, *args, **kwargs):
        return func(*args, **kwargs)

    # --- Jump Search ---
    @staticmethod
    def jump_search(arr, target):
        n = len(arr)
        jump = int(math.sqrt(n))
        left, right = 0, 0

        while right < n and arr[right] < target:
            left = right
            right += jump

        for i in range(left, min(right, n)):
            if arr[i] == target:
                return i

        return -1

    @staticmethod
    def jump_search_wrapper(func, *args, **kwargs):
        return func(*args, **kwargs)

    # --- Ternary Search ---
    @staticmethod
    def ternary_search(arr, target, left, right):
        if left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            if arr[mid1] == target:
                return mid1
            elif arr[mid2] == target:
                return mid2
            elif target < arr[mid1]:
                return SearchAlgorithms.ternary_search(arr, target, left, mid1 - 1)
            elif target > arr[mid2]:
                return SearchAlgorithms.ternary_search(arr, target, mid2 + 1, right)
            else:
                return SearchAlgorithms.ternary_search(arr, target, mid1 + 1, mid2 - 1)

        return -1

    @staticmethod
    def ternary_search_wrapper(func, *args, **kwargs):
        return func(*args, **kwargs)