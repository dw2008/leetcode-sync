class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int result = 0;
        for(int i = 0; i < nums.size(); i++){
            unsigned int number_of_digits = 0;
            do {
                ++number_of_digits; 
                nums[i] /= 10;
            } while (nums[i]);
            if (number_of_digits % 2 == 0){
                result ++;
            }
        }
        return result;
    }
};