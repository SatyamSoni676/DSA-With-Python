#https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        num = 0
        for i in nums:
            if count == 0:
                num = i
            if i == num:
                count += 1
            else:
                count -= 1
        return num
