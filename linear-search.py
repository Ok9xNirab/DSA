def linear_search():
    """
    Perform a linear search on a list of elements.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    # Example implementation
    def search(arr, target):
        for index, element in enumerate(arr):
            if element == target:
                return index
        return -1

    # Example usage
    arr = [5, 3, 8, 6, 2]
    target = 6
    result = search(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found.")

linear_search()