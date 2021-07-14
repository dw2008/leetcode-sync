class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(),satisfaction.end());
        int n = satisfaction.size(),sum=0;
        for(int i=n-1;i>0;i--)
            satisfaction[i-1]+=satisfaction[i];
        int i=0;
        while(i<n){
            if(satisfaction[i]>=0) sum+=satisfaction[i];
            i++;
        }
        return sum;
        }
};