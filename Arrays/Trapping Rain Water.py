#https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        sum_s, lmax, rmax = 0, 0, 0
        n = len(height)
        left, right = 0, n-1

        while left <= right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])

            if lmax > rmax:
                sum_s += rmax - height[right]
                right -= 1
            else:
                sum_s += lmax - height[left]
                left += 1
            
        return sum_s
