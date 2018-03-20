#!/usr/local/bin/python3

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        length = len(nums)
        for i in range(length):
            if target-nums[i] in dict:
                return [dict[target-nums[i]], i]
            dict[nums[i]] = i

print (Solution().twoSum([2,3,4],6))

