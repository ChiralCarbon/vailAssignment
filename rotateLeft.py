def rotateLeft(arr, positions):
    # Check if positions is negative
    if positions < 0:
        raise ValueError("Positions to rotate cannot be negative")
    
    # Handle cases where positions > length of array, using modulus
    positions = positions % len(arr)
    
    # Reverse the first part of the array in-place without using any temporary variables
    reverse(arr, 0, positions - 1)
    # Reverse the second part of the array in-place
    reverse(arr, positions, len(arr) - 1)
    # Reverse the whole array to get our solution
    reverse(arr, 0, len(arr) - 1)
    
    return arr

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
