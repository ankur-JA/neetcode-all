class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int> newNums;

        for(int i=0; i<nums.size(); i++) {
            if(nums[i] != val) {
                newNums.push_back(nums[i]);
            }
        }
        int n = nums.size() - newNums.size();
        for(int i=0; i<newNums.size(); i++) {
            nums[i] = newNums[i];
        }

        for(int i=0; i<n; i++) {
            nums.pop_back();
        }

        return nums.size();
    }
};