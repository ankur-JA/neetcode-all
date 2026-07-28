class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # n = len(arr)
        
        # for i in range(0, n-1):
        #     temp = arr[i+1]
        #     for j in range(i+1, n):
        #         if arr[j] >= temp:
        #             temp = arr[j]
        #     arr[i] = temp
        
        # arr[n-1] = -1
        # return arr
        right_max = -1

        for i in range(len(arr) - 1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max

        return arr