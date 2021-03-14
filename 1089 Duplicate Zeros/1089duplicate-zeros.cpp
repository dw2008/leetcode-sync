class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int count = 0, n = arr.size();
        for(int i = 0; i < n; i++){
            if(arr[i] == 0){
                count ++;
            }
        }
        for(int i = n - 1, j = n - 1 + count; i >= 0; --i, --j){
            if(j < n){
                arr[j] = arr[i];
            }
            if(arr[i] == 0 && --j < n){
                arr[j] = 0;
            }
        }
    }
};