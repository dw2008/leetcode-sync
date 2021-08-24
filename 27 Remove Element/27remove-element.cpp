class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if(nums.size() == 0){ 
            return 0;
        }
        size_t cnt = 0;
        for(size_t i=0; i < nums.size(); i++) {
          if(nums[i] != val){
            nums[cnt++] = nums[i];
          }
        }
        return cnt;
    }
};