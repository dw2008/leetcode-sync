class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool result = true;
        for(int i = 0; i < nums.size() - 1; i++){
            if(nums[i] > nums[i + 1]){
                result = false;
            }
        }
        if(result == false){
            bool mark = true;
            for(int i = nums.size() - 1; i > 0; i--){
                if(nums[i] > nums[i - 1]){
                    mark = false;
                }
            }
            if(mark == true){
                result = true;
            }
        }
        return result;
    }
};