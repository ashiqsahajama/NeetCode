class Solution {
public:
    int maxConsecutive(int bottom, int top, vector<int>& special) {
        sort(special.begin(),special.end());
        int res = 0;
        res = max(res,abs(bottom-special[0]));

        for(int i=1;i<special.size();i++){
            res= max(res,special[i]-special[i-1]-1);
        }
        res = max(res,abs(top-special[special.size()-1]));

        return res;
    }
};
