#!/usr/local/bin/python3

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i,item in enumerate(nums):
            if target-item in dict:
                return [dict[target-item], i]
            dict[item] = i

print (Solution().twoSum([2,3,4],6))

