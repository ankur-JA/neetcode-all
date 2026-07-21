class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> newArray;

        newArray.push_back(nums[0]);

        for(int i=1; i<nums.size(); i++) {
            if(nums[i-1] != nums[i]) {
                newArray.push_back(nums[i]);
            }
        }

        for(int i=0; i<newArray.size(); i++) {
            nums[i] = newArray[i];
        }

        return newArray.size();
    }
};