#!/usr/local/bin/python3

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = list(s)
        substr = []
        max = length = 0
        for c in str:
            if c not in substr:
                substr.append(c)
                length += 1
            else:
                rm_len = substr.index(c) + 1
                length = length + 1 - rm_len
                while(rm_len):
                    substr.pop(0)
                    rm_len -= 1
                substr.append(c)

            max = length if length > max else max

        return max 


string = 'aab'
print(Solution().lengthOfLongestSubstring(string))
