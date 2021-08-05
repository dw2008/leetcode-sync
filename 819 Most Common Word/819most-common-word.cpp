class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        string result;
        int count = 0;
        unordered_map<string, int> umap;
        int i = 0;
        while(i < paragraph.size()){
            string result = "";
            while(i < paragraph.size() && isalpha(paragraph[i])){
                result += tolower(paragraph[i]);
                i++;
            }
            if(result != "")
                umap[result]++;
            i++;
        }
        for(auto& s: banned){
            umap.erase(s);
        }
        for(auto& [key,value] : umap){
            if(count < value){
                result = key;
                count = value;
            }
        }
        return result;
    }
};