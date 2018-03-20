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
            dict[nums[i]] = i

        for i in range(length):
            if target-nums[i] in dict:
                if dict[target-nums[i]] != i:
                    return [i,dict[target-nums[i]]]



print (Solution().twoSum([2,3,4],6))

