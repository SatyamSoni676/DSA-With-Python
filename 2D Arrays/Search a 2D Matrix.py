#https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, (m*n)-1
        while l <= r:
            mid = (l+r)//2
            matrix_mid = matrix[mid//m][mid % m]
            if matrix_mid == target:
                return True
            elif matrix_mid > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
