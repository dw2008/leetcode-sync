class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        string temp;
        for (auto word : strs) {
            temp = word;
            sort(temp.begin(), temp.end());
            m[temp].push_back(word);
        }
        vector<vector<string>> res;
        for (auto [word, list] : m) {
            res.push_back(list);
        }
        return res;
    }
};