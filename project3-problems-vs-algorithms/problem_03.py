def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_arr = merge_sort(input_list)

    num1 = 0
    num2 = 0

    if len(sorted_arr) % 2 == 1:
        num1 = num1 * 10 + sorted_arr.pop()

    start = len(sorted_arr) - 1
    while start >= 0:
        num1 = num1 * 10 + sorted_arr[start]
        num2 = num2 * 10 + sorted_arr[start - 1]
        start -= 2

    return [num1, num2]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    print('output: ', output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 2], [1, 2]])