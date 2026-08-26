import math as Math

def binary_search():
    """
    Perform a binary search on a sorted list of elements.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    def search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = Math.floor((left + right) / 2)
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # Example usage
    arr = [2, 3, 5, 6, 8]
    target = 6
    result = search(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found.")