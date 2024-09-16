#  class Solution {
#  public:
#      vector<int> twoSum(vector<int>& nums, int target) {
#          unordered_map<int,int> n;
#          vector<int> res;

#          for(int i=0;i<nums.size();i++){
#              if(n.find(target-nums[i])!=n.end()){
#                  res.push_back(i);
#                  res.push_back(n[target-nums[i]]);
#              }
#              else{
#                 n.insert({nums[i],i});
#                  //n[nums[i]]==i;
#              }
#          }
#          return res;
#      }
#  };

# if target-num[i] in dictionary then return i,value of target-num[i] from dictioanry else insert num[i] as key and i value.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        b =[]
        
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [i,d[target - nums[i]]]
            else:
                d[nums[i]] = i



        return b    
