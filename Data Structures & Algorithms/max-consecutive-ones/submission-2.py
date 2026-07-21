class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        value = 0

        for i in nums:
            if i == 1:
                value += 1

            if i == 0:
                max_count = max(max_count, value)
                value = 0
              
        return max(max_count, value)


        

