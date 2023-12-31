#https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []

        for index, value in enumerate(temperatures):
            while stack and stack[-1][1] < value:
                temp_index, temp_value = stack.pop()
                ans[temp_index] = index - temp_index
            stack.append([index, value])

        return ans
