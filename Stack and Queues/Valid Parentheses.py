#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        patterns = ['()', '{}', '[]']
        while len(s) > 0:
            l = len(s)
            for pattern in patterns:
                s = s.replace(pattern, '')
            if l == len(s):
                return False
        return True
