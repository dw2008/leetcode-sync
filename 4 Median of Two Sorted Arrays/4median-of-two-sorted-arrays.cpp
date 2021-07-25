class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        vector<int> total;
        for(int i = 0; i < n; i++){
            total.push_back(nums1[i]);
        }
        for(int j = 0; j < m; j++){
            total.push_back(nums2[j]);
        }
        sort(total.begin(), total.end());
        double result;
        int s = total.size();
        double d = 2;
        if(s % 2 == 0){
            result = (total[s/2] + total[s/2 -1])/d;
        }
        if(s % 2 != 0){
            result = total[s/2];
        }
        return result;
    }
};