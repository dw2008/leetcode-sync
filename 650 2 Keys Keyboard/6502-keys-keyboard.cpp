class Solution {
public:
    int minSteps(int n) {
        int current = 1;
        int previous = 0;
        int result = 0;
        while(current < n){
            if(n % current == 0){
                previous = current;
                current += previous;
                result += 2;
            }
            else{
                current += previous;
                result++;
            }
        }
        return result;
    }
};