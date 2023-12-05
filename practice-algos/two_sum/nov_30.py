def twoSum(number, target):
    num_map ={}
    for index, number in enumerate(number):
        difference_between_num_and_target = target - number
        if difference_between_num_and_target in num_map:
            print(difference_between_num_and_target, number, target)
            return [num_map[difference_between_num_and_target], index]
        num_map[number] = index
        # print(num_map)

print(twoSum([2,1,4,5,3], 9))