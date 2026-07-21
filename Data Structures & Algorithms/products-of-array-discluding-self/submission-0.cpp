class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> forward(n), backward(n), res(n);

        // forward[i] = product of all elements before index i
        forward[0] = 1;
        for (int i = 1; i < n; i++) {
            forward[i] = forward[i - 1] * nums[i - 1];
        }

        // backward[i] = product of all elements after index i
        backward[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            backward[i] = backward[i + 1] * nums[i + 1];
        }

        // result[i] = product of all elements except nums[i]
        for (int i = 0; i < n; i++) {
            res[i] = forward[i] * backward[i];
        }

        return res;
    }
};
