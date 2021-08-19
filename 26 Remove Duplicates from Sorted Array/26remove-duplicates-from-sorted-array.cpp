class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        size_t cnt = 1;
        for(size_t i = 1; i < nums.size(); i++) {
          if(nums[i] != nums[cnt-1])
            nums[cnt++] = nums[i];
        }
        return cnt;
    }
};