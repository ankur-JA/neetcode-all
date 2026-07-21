class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0

        for num in nums:
            res = max(res, cnt)
            if num == 0:
                cnt = 0
            else:
                cnt += 1

        return max(res, cnt)

        

