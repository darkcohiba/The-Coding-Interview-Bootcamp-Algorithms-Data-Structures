def hammingWeight(n: int) -> int:
    tot = 0
    while n:
        print("first n ", n)
        tot += n & 1
        n >>= 1
        print("second n ",n)

        
    return tot

print(hammingWeight(0b00000000000000000000000000001011))
# print(hammingWeight(0b00000000000000000000000010000000)) 
# print(hammingWeight(0b11111111111111111111111111111101))
