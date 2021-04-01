class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> sortedArray(A.size());
        int indexEven = 0;
        int indexOdd = A.size() -1;
        
        for (int index = 0; index < A.size(); index++) {
            if (A[index] % 2 == 0) {
                sortedArray[indexEven] = A[index];
                indexEven += 1;
            } else {
                sortedArray[indexOdd] = A[index];
                indexOdd -= 1;
            }
        }
        return sortedArray;
    }
};