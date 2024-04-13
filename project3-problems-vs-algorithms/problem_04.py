def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low = 0  # pointer_0
    mid = 0  # pointer_1
    high = len(input_list) - 1  # pointer_2

    while mid <= high:
        if input_list[mid] == 0:
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        else:
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test case where the input list is empty
test_function([])

# Test case where the input list contains only one element
test_function([0])

# Test case where the input list contains only one type of element
test_function([0, 0, 0, 0])

# Test case where the input list contains elements in descending order
test_function([2, 1, 0])

# Test case where the input list contains elements in ascending order
test_function([0, 1, 2])

# Test case where the input list contains a large number of elements
test_function([2] * 1000000 + [1] * 1000000 + [0] * 1000000)
