class Solution {
public:
    bool isPalindrome(int x) {
        string a = to_string(x);
        bool result = true;
        for(int i = 0; i < a.length()/2; i++){
            if(a[i] != a[a.length() - 1 - i]){
                result = false;
            }
        }
        return result;
    }
};