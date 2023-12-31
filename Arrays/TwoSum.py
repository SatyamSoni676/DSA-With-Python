#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in d1:
                return [d1[diff], i]
            d1[nums[i]] = i
        return []
