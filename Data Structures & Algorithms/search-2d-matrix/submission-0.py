class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for n in matrix:
            ans = self.binarySearch(n, target)
            if ans:
                return True
    
        return False

    def binarySearch(self, arr: List[int], target: int) -> bool:
        L, R = 0, len(arr) - 1

        while L<=R:
            m = (L+R)//2

            if target < arr[m]:
                R = m-1
            elif target > arr[m]:
                L = m+1
            else:
                return True

        return False