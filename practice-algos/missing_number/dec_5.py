def missingNumber(nums) -> int:
    n = len(nums) + 1
    real_sum = sum(nums)
    expected_sum = 0
    for index in range(n):
        expected_sum += index
    return expected_sum - real_sum
    



    # real_sum = sum(nums)
    # expected_sum = 0
    # for index in range(len(nums) + 1):
    #     print(index)
    #     expected_sum += index
    # print(expected_sum)
    # print(real_sum)
    # return expected_sum - real_sum
print(missingNumber([3,0,1]))
print(missingNumber([0,1]))
print(missingNumber([3,0,1,4,5,6,7,9,2]))