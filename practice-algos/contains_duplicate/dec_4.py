def containsDuplicate(nums):
    num_map = {}
    for index, num in enumerate(nums):
        print(num_map)
        if num in num_map:
            print('inside the true ', num)
            return True
        else:
            print('inside the not true ', num)
            num_map[num] = index
    return False

print(containsDuplicate([22,2,3,4,22]))