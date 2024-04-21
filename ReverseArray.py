def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

arr = [5,6,7,8,9,1]
print("Original Array:", arr)
reversed_arr = reverse_array(arr)
print("Reversed Array:", reversed_arr)