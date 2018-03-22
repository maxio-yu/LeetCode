#!/usr/local/bin/python3

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        while (1):
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    merged.append(nums1.pop(0))
                else:
                    merged.append(nums2.pop(0))
            elif nums1:
                merged.extend(nums1)
                break
            elif nums2:
                merged.extend(nums2)
                break

        mid, odd = divmod(len(merged),2)
        if odd:
            return merged[mid]
        else:
            return (merged[mid] + merged[mid-1])/2


a=[1,3,5]
b=[2,4,6]
Solution().findMedianSortedArrays(a,b)
