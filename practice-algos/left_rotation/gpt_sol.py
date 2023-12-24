def left_rotate(arr, d):
    n = len(arr)
    d = d % n  # This line handles cases where d > n
    return arr[d:] + arr[:d]

# Example usage
arr = [1, 2, 3, 4, 5]
d = 2
result = left_rotate(arr, d)
print("Rotated Array:", result)
