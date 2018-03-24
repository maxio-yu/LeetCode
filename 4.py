#!/usr/local/bin/python3

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)


        imin, imax = 0, m
        half,odd = divmod(m+n,2)
        while(imin <= imax):
            i = (imin+imax)//2
            j = half - i
            # left_A has element
            if i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            # left_B has element
            elif i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            else:
                break

        j = half - i

        # A has no right part
        if i == m:
            min_right = nums2[j]
        # B has no right part
        elif j == n:
            min_right = nums1[i]
        else:
            min_right = min(nums1[i], nums2[j])

        if odd:
            return min_right
        else:
            # A has no left part
            if i == 0:
                return (nums2[j-1] + min_right)/2
            # B has no left part
            elif j == 0:
                return (nums1[i-1] + min_right)/ 2
            else:
                return (max(nums1[i-1],nums2[j-1]) + min_right)/ 2



a=[6,7,8]
b=[1,2,3,4,5]
a=[1,3]
b=[2]
a=[]
b=[3,4]
a=[1,2]
b=[3,4]
print(Solution().findMedianSortedArrays(a,b))
