class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dic = {}
        ans=0
        for i in range(0,len(nums),2):
            if(nums[i] in dic):
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        dic1 = {}
        for i in range(1,len(nums),2):
            if(nums[i] in dic1):
                dic1[nums[i]]+=1
            else:
                dic1[nums[i]]=1
        dicsum = sum(dic.values())
        dic1sum = sum(dic1.values())
        d1 = [(i,dic[i]) for i in dic.keys()]
        d2 = [(i,dic1[i]) for i in dic1.keys()]
        d1 = sorted(d1,key= lambda x:x[1],reverse=True)
        d2 = sorted(d2,key=lambda x:x[1],reverse=True)
        for i in d1:
            for j in d2:
                if(i[0]!=j[0]):
                    return dicsum-i[1]+dic1sum-j[1]
        return min(dicsum,dic1sum)
