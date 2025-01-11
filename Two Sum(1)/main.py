class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            for x in range(i+1, len(nums)):
                if nums[i] + nums[x] == target:
                    result = [i, x]
                    return result