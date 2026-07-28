class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        for i in range(0, n-1):
            temp = arr[i+1]
            for j in range(i+1, n):
                if arr[j] >= temp:
                    temp = arr[j]
            arr[i] = temp
        
        arr[n-1] = -1
        return arr