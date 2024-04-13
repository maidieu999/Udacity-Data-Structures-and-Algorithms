def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    length = len(input_list)

    if length == 0:
        return -1

    if length == 1 and input_list[0] == number:
        return 0

    start = 0
    end = length - 1

    while start <= end:
        mid = (start + end) // 2
        if input_list[mid] == number:
            return mid
        
        if input_list[start] <= input_list[mid]:
            if input_list[start] <= number < input_list[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if input_list[mid] < number <= input_list[end]:
                start = mid + 1
            else:
                end = mid - 1
    
    return -1
        

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test case where the target number is not present in the array
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 5])

# Test case where the array is empty
test_function([[], 10])

# Test case where the target number is larger than any element in the array
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 11])

# Test case where the target number is smaller than any element in the array
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 0])

# Test case where the target number is present at the beginning of the array
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

# Test case where the target number is present at the end of the array
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 4])

# Test case where the array contains only one element and it matches the target number
test_function([[6], 6])

# Test case where the array contains only one element and it doesn't match the target number
test_function([[6], 7])
