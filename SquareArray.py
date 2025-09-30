# Given a sorted array, create a new array containing squares of all the numbers of the input array in sorted order.

# [1,3,5] => [1,9,25]
# [0,5,6] => [0,25,36]
# [-4,-2,0,1,3] => [0,1,4,9,16]

# Method 1  Brute Force
# Time Complexity: O(n log n)
# Space Complexity: O(n)

'''def square_array(arr):
    result = []
    for num in arr:
        result.append(num * num)
    return sorted(result)'''

# Method 2  
# Time Complexity: O(n)
# Space Complexity: O(n)

def square_array(arr):
    n = len(arr)
    i,j = 0, len(arr) - 1
    res = [0] * n
    for k in reversed(range(n)):
        if arr[i] ** 2 > arr[j] ** 2:
            res[k] = arr[i] ** 2
            i += 1
        else:
            res[k] = arr[j] ** 2
            j -= 1
    return res
print(square_array([1, 3, 5]))
print(square_array([0, 5, 6]))  
print(square_array([-4, -2, 0, 1, 3]))
