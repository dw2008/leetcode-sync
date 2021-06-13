class Solution {
public:
    int climbStairs(int n) {
        if (n < 3) {
            return n;
        }
        int a = 1;
        int b = 2;
        int result;
        for (int i = 3; i <= n; i++) {
           result = b + a;
           a = b;
            b = result;
        }

        return result;
    }
};