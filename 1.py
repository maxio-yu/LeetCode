#!/usr/local/bin/python3

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(0, length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]



print (Solution().twoSum([3,2,4],6))

