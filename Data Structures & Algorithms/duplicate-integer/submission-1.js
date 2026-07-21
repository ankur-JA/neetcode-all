class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let unique = Array.from(new Set(nums));

        if(unique.length < nums.length) {
            return true;
        } else {
            return false;
        }
    }
}
