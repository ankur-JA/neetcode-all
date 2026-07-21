class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;
        int n = nums.size();

        for(int i=0; i<2*n; i++){
            if(i >= n) {
                ans.push_back(nums[i-n]);
                continue;
            }
            ans.push_back(nums[i]);
        }

        // for(int i=n; i<2*n; i++) {
        //     ans.push_back(nums[i-n]);
        // }

        return ans;
    }
};