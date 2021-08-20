class Solution {
public:
    int strStr(string haystack, string needle) {
        size_t result = haystack.find(needle);
        return result;
    }
};