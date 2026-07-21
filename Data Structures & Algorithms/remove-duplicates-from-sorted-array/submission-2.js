class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        // Method - 1 using Set
        // let unique = Array.from(new Set(nums)).sort((a,b) => a - b);
        // for(let i=0; i<unique.length; i++) {
        //     nums[i] = unique[i];
        // }

        // return unique.length;

        // Method - 2 using two pointer My - sefl but it is not good code 
        // let l = 1;
        // for(let r=0 ;r<nums.length; r++) {
        //     if(nums[r] != nums[r+1]) {
        //         nums[l] = nums[r+1];
        //         l++;
        //     }
        // }

        // return l-1;

        // Method - 2 using two pointer - 1
        let n = nums.length;
        let l = 0;
        let r = 0;
        while(r<n) {
            nums[l] = nums[r];
            while(r<n && nums[r] === nums[l]) {
                r++;
            }
            l++;
        }
        return l;
    }
}
