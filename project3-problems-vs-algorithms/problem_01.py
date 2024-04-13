def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        raise ValueError("Square root is not defined for negative numbers")

    if number < 2:
        return number
    
    start = 1
    end = number

    while start <= end:
        mid = (start + end) // 2

        if mid * mid == number:
            return mid
        elif mid * mid < number:
            start = mid + 1
            result = mid
        elif mid * mid > number:
            end = mid - 1

    return result

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Input Validation: Negative Number
try:
    sqrt(-1)
    print("Fail: No exception raised for negative number")
except ValueError:
    print("Pass: ValueError raised for negative number")
