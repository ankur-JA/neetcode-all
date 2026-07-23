class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_arr = []

        for num in nums:
            if num != val:
                new_arr.append(num)
        
        for i in range(len(new_arr)):
            nums[i] = new_arr[i]


        return len(new_arr)