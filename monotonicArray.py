# Monotonic Array Problem
# Determine if an array is monotonic (entirely non-increasing or non-decreasing).
# [1,2,2,3] => True
# [6,5,4,4] => True 
# [1,3,2] => False
# [1,2,4,5] => True

# Method 1  
# Time Complexity: O(n)
# Space Complexity: O(1)

def is_monotonic(arr):
    n = len(arr)
    if n == 0:
        return True
    first = arr[0]
    last = arr[n-1]
    if first > last:
        for k in range(n-1):
            if arr[k] < arr[k+1]:
                return False
    elif first == last:
        for k in range(n-1):
            if arr[k] != arr[k+1]:
                return False
    else:
        for k in range(n-1):
            if arr[k] > arr[k+1]:
                return False        

    return True

print(is_monotonic([1, 3, 2]))
print(is_monotonic([1, 2, 4, 5]))
print(is_monotonic([1, 2, 2, 3]))
print(is_monotonic([6, 5, 4, 4]))
