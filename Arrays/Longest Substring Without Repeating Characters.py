#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_S = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in char_S:
                char_S.remove(s[l])
                l+=1
            char_S.add(s[r])
            res = max(res, r-l+1)
        return res
