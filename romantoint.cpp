class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> rom;
        rom['I'] = 1;
        rom['V'] = 5;
        rom['X'] = 10;
        rom['L'] = 50;
        rom['C'] = 100;
        rom['D'] = 500;
        rom['M'] = 1000;
     vector<string> st;
    //  for(int i=0;i<s.size();i++){
    //      st.push_back({s[i]});
    //  }
        int res = 0;
     for(int i=0;i<s.size();i++){
         if( rom[s[i]] < rom[s[i+1]] ){
             res-=rom[s[i]];
         }
         else{
            res += rom[s[i]];
         }
     }
    
    return res;
    }
};
