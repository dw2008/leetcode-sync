class Solution {
    public int minOperations(String[] logs) {
        int n = 0;
        for(String s: logs){
            if(s.equals("../")){
                if(n > 0){
                    n--;
                }
            }
            else if(!s.equals("./")){
                n++;
            }
        }
        return n;
    }
}