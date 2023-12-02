#https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path, res):
            if len(path) == k:
                res.append(path.copy())     
            for i in range(start, n+1):
                path.append(i)
                backtrack(i+1, path, res)
                path.pop()
        res = []
        backtrack(1, [], res)
        return res 
