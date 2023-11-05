
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>m;
        for(int i=0;i<nums.size();i++){
            if(m.find(nums[i])!=m.end()){
                m[nums[i]]++;
            }
            else{
                m[nums[i]]=1;
            }
        }
        priority_queue<pair<int,int>> res;
        for(auto&i:m){
            res.push({i.second,i.first});
        }
        vector<int> ans;
        while(k>0){
            ans.push_back({res.top().second});
            res.pop();
            k--;
        }    
    return ans;
    }
};


// create a dict for frequency and priority queue for getting the top element.
