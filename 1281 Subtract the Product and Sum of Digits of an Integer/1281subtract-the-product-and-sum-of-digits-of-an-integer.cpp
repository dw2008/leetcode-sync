class Solution {
public:
    int subtractProductAndSum(int n) {
        string num = to_string(n);
        int product = 1, sum = 0;
        if(n == 0){
            return 0;
        }
        for(int i = 0; i < num.length(); i++){
            int temp = num[i] - '0';
            product *= temp;
            sum += temp;
        }
        return product - sum;
    }
};