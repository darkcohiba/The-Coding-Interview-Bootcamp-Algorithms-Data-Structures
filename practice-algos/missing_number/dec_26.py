def missingNumber(nums):
    # get the length of the array plus 1 so we can loop
    n = len(nums) + 1
    real_sum = sum(nums)
    expected = 0
    for index in range(n):
        expected += index
    return expected - real_sum


print(missingNumber([3,0,1]))
print(missingNumber([0,1]))
print(missingNumber([3,0,1,4,5,6,7,9,2]))