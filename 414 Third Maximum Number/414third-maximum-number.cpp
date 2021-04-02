class Solution {
public:
    int thirdMax(vector<int>& nums) {
    int *a, *b, *c;
      a = b = c = NULL;
      for (int i = 0; i < nums.size(); ++i) {
         if (!a || nums[i] >= *a) {
            if (a && nums[i] > *a) {
               c = b;
               b = a;
            }
            a = &nums[i];
         }
         else if (!b || nums[i] >= *b) {
            if (b && nums[i] > *b) {
               c = b;
            }
            b = &nums[i];
         }
         else if (!c || nums[i] >= *c) {
            c = &nums[i];
         }
      }
      return !c ? *a : *c;
    }
};