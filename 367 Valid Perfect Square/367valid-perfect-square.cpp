class Solution {
public:
    bool isPerfectSquare(int num) {
        float result;
        result = sqrt(num);
        if(int(result) != result){
            return false;
        }
        return true;
    }
};