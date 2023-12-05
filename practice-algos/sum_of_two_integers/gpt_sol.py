def getSum(a, b):
    # 32 bits integer max
    MASK = 0xFFFFFFFF
    # Max integer
    INT_MAX = 0x7FFFFFFF
    
    while b != 0:
        # XOR operation gives the sum without considering carry.
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    # If a is negative, we return the two's complement of a.
    return a if a <= INT_MAX else ~(a ^ MASK)

# Test cases
print(getSum(1, 2))  # Output: 3
print(getSum(2, 3))  # Output: 5
