#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        max_Water = 0

        while start < end:
            curr_Water = min(height[start], height[end]) * (end - start)
            if curr_Water > max_Water:
                max_Water = curr_Water
            if height[start] < height[end]:
                start+=1
            else:
                end-=1

        return max_Water
