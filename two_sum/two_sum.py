def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
target = 9
nums = [2, 7, 11, 15]
print(two_sum_brute(nums=nums,target=target))           