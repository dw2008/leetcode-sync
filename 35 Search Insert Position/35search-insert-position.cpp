class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size(); i++){
            if (nums[i] == target)
                return i;
        }
        for(int i = 0; i < nums.size() - 1; i++){
            if(target > nums[i] && target < nums[i + 1])
                return i + 1;
        }
        if(target > nums[nums.size() - 1])
            return nums.size();
        return 0;
    }
};