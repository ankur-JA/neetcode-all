class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Method - 1 Brute Force
        // int n = nums.size();
        // for(int i=0; i<n-1; i++) {
        //     for(int j=i+1; j<n; j++) {
        //         if(nums[i] == nums[j]) {
        //             return true;
        //         }
        //     }
        // }

        // return false;

        // Method -2 using the sorting an array

        // sort(nums.begin(), nums.end());
        // int n = nums.size();
        // for(int i=0; i<n-1; i++) {
        //     if(nums[i] == nums[i+1]) {
        //         return true;
        //     }
        // }

        // return false;


        // Method - 3 using the unordered_set

        unordered_set<int> seen;
        for(int num : nums) {
            if(seen.count(num)) {
                return true;
            }

            seen.insert(num);
        }

        return false;
    }
};