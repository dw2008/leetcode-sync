class Solution {
public:
    vector<string> letterCombinations(string digits) {
        const vector<string> m = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        if(digits.size() == 0){
            return {};
        }
        vector<string> result;
        result.push_back("");
        for(auto a: digits) {
            vector<string> temp;
            for(auto x: m[a - '0']) {
                for(auto b: result) {
                    temp.push_back(b + x);
                }
            }
            result.swap(temp);
        }
        return result;
    }
};