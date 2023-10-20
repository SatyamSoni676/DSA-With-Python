#https://leetcode.com/problems/kth-largest-element-in-an-array/

import queue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = queue.PriorityQueue()
        for i in nums:
            pq.put(i)
            if pq.qsize() > k:
                pq.get()
        return pq.get()
