#!/usr/local/bin/python4

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        length = len(s)
        ret = ''
        for row in range(numRows):
            delta1 = (numRows - row - 1) * 2
            delta2 = row * 2 
            i = row
            if i < length:
                ret += s[i]
            while (i < length):
                if delta1:
                    i = i + delta1
                    if i < length:
                        ret += s[i]
                if delta2:
                    i = i + delta2
                    if i < length:
                        ret += s[i]

        return ret

s = 'PAYPALISHIRING'
n = 3
s = 'A'
n = 1
print(Solution().convert(s,n))



