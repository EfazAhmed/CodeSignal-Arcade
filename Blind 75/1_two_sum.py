class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i != j:
                    total = nums[i] + nums[j]
                    if total == target:
                        return [i,j]
        return None

