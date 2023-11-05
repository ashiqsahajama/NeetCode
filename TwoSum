class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> n;
        vector<int> res;

        for(int i=0;i<nums.size();i++){
            if(n.find(target-nums[i])!=n.end()){
                res.push_back(i);
                res.push_back(n[target-nums[i]]);
            }
            else{
                n.insert({nums[i],i});
                //n[nums[i]]==i;
            }
        }
        return res;
    }
};
