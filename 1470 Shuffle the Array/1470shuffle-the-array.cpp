class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> result;
        for(int x=0; x < n; x++){
            result.push_back(nums[x]);
            result.push_back(nums[n+x]);
        }
        return result;
    }
};