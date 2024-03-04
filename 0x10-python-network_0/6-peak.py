def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers: List of unsorted integers

    Returns:
    - The peak element
    """
    list_int = list_of_integers
    if not list_int:
        return None
    length = len(list_int)

    low, high = 0, length - 1

    while low < high:
        mid = low + (high - low) // 2
        if list_int[mid] > list_int[mid - 1] and list_int[mid] > list_int[mid + 1]:
            return list_int[mid]
        if list_int[mid - 1] > list_int[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_int[low]
