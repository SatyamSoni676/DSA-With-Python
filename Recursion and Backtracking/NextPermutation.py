#https://leetcode.com/problems/next-permutation/


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        b1 = -1

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                b1 = i

        if b1 == -1:
            nums.reverse()
            return nums

        for j in range(len(nums) - 1, b1, -1):
            if nums[j] > nums[b1]:
                nums[j], nums[b1] = nums[b1], nums[j]
                break

        nums[b1+1:] = reversed(nums[b1+1:])
