#!/usr/local/bin/python3

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_l = start = 0
        c_index = {}
        for i,c in enumerate(s):
            # c need in the sub string which start from start
            if c in c_index and start <= c_index[c]:
                start = c_index[c] + 1
            else:
                max_l = max(max_l, i-start+1)

            c_index[c] = i

        return max_l 


string = 'abcabcbb'
print(Solution().lengthOfLongestSubstring(string))
