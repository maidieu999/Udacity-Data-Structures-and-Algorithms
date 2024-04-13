def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    Returns:
       tuple: A tuple containing the minimum and maximum elements in the input list
    """
    if not ints:
        return None

    min_val = max_val = ints[0]

    for num in ints[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test case where the input list is empty
print("Edge Test: Empty List")
print("Pass" if get_min_max([]) == None else "Fail")

# Test case where the input list contains only one element
print("\nEdge Test: Single Element List")
print("Pass" if get_min_max([5]) == (5, 5) else "Fail")

# Test case where the input list contains negative numbers
print("\nEdge Test: Negative Numbers")
print("Pass" if get_min_max([-5, -10, -3, -7]) == (-10, -3) else "Fail")

# Test case where the input list contains duplicate elements
print("\nEdge Test: Duplicate Elements")
print("Pass" if get_min_max([5, 3, 5, 9, 3, 9]) == (3, 9) else "Fail")

# Test case where the input list contains large numbers
print("\nEdge Test: Large Numbers")
large_list = [random.randint(0, 1000000) for _ in range(1000000)]
print("Pass" if get_min_max(large_list) == (min(large_list), max(large_list)) else "Fail")
