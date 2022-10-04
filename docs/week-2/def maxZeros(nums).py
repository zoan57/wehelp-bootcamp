def maxZeros(nums):
    count = 0
    result = 0
    for i in range(len(nums)):
        if nums[i]==1:
            count=0
        else:
            count+=1
            result = max(result, count)
    print(result)
    
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]); #得到 0
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([0, 0, 0, 1, 1]) # 得到 3
maxZeros([1, 1, 1, 0]) # 得到 1