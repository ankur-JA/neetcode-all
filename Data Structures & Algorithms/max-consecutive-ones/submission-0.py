class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        counter = 0;

        for num in nums:
            if num == 1:
                counter += 1
                max_count = max(max_count, counter)
            else:
                counter = 0
        
        return max_count


