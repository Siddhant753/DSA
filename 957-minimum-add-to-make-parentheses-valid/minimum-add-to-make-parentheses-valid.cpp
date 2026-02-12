class Solution {
public:
    int minAddToMakeValid(string s) {
        int opened = 0;
        int closed = 0;
        int n = s.length();
        for(int i=0; i<n; i++){
            if (s[i] == '('){
                opened ++;
            }
            else{
                if (opened > 0){
                    opened --;
                }
                else{
                    closed ++;
                }
            }
        }
        return opened + closed;
    }
};