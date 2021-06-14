class Solution {
public:
    bool isValid(string s) {
        map<char,char>m;
        m['(']=')';
        m['{']='}';
        m['[']=']';
        int i;
        string c="";
        int j;
        for(i=0;i<s.length();i++){
            if((s[i]=='(')||(s[i]=='{')||(s[i]=='[')){
               c=c+(s.at(i));
            }else if((s[i]==')')||(s[i]=='}')||(s[i]==']')){
                j=c.length();
                if(j==0){
                    return false;
                }
                if(m[c[j-1]]!=s[i]){
                    return false;
                }else{
                  c= c.substr(0,j-1);
                }
            }
        }
        if(c.length()){
            return false;
        }
        return true;
    }
};