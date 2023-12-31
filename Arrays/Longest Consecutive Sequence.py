#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_count = 0
        n1, count = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == n1 + 1:
                count+=1
                n1 = nums[i]
            elif nums[i] == n1:
                continue
            else:
                max_count = max(max_count, count)
                n1, count = nums[i], 1

        return max(max_count, count)
