def hamming_weight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Test cases
print(hamming_weight(0b00000000000000000000000000001011)) # 3
print(hamming_weight(0b00000000000000000000000010000000)) # 1
print(hamming_weight(0b11111111111111111111111111111101)) # 31
