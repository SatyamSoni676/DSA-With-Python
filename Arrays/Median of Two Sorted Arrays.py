#https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = nums1 + nums2
        num3.sort()
        low = 0
        high = len(num3)-1
        while low < high:
            low += 1
            high -= 1

        if low == high:
            return float(num3[low])
        else:
            return float((num3[low]+num3[high])/2)
