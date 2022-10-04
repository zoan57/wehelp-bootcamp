def twoSum(nums, target):
    for i in range(len(nums)):
        second_number = target - nums[i]
        if (second_number in nums):
            second_index = nums.index(second_number)
            if (i !=second_index):
                return sorted([i, second_index])
    
    
result=twoSum([2, 11, 7, 15], 9)
print(result)
