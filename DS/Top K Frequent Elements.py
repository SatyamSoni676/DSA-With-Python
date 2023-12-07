#https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1, s = {}, []
        for i in nums:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        
        for num, freq in sorted(d1.items(), key = lambda x:x[1], reverse = True):
            s.append(num)
        return s[:k]