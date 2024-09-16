# So the problem is to find the max repeating K numbers from the array.

#Approach one is to create a dictionary with key as the numbers and values as number of repeatations.
#The sort the dictionary based on values and get the keys in a array.This can be done using sorted function
# sorted takes array to iterate, key that takes what to sort the array to sort based on and here we sort based on values.
#then return the top k elements


#Approach 2 is to use bucket sort.Create a array with arrays with number of elements in input and place keys on the new array with value as the index.
#return the array.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict ={}
        # arr = []
        # for i in range(len(nums)+1):
        #     arr.append([])

        for i in nums:
            if dict.get(i)!=None:
                dict[i]+=1
            else:
                dict[i]=1
        sortres = []
        sortres = sorted(dict,key=dict.get,reverse=True)
        return sortres[:k]
        # for num,count in dict.items():
        #     arr[count].append(num)
        # res = []
        # for i in range(len(nums),0,-1):
        #     for n in arr[i]:
        #         res.append(n)
        #         if len(res)==k:
        #             return res

