def maxProduct(nums):
    n = len(nums) #deifne the length of the list so that we can call it.
    nums.sort() 
    neg_max = nums[0]*nums[1] 
    pos_max = nums[n-1]*nums[n-2]
    if (neg_max > pos_max):
        print(neg_max)   
    else:
        print(pos_max)
                 
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10