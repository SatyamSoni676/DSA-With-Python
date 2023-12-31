#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d1 = {}
        n = len(nums)
        
        for i in nums:
            if i in d1:
                return True
            d1[i] = 1
        return False
