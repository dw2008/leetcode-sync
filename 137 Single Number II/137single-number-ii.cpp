class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map <int, int> map;
        for (auto i : nums){
            map[i]++;
        }
        for (auto it : map){
            if (it.second == 1){
                return it.first;
            }
        }
        return 0;
    }
};