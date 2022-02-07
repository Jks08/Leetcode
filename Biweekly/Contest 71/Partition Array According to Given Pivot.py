class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s=[]
        s1=[]
        s2=[]
        for i in nums:
            if(i<pivot):
                s.append(i)
            elif(i==pivot):
                s1.append(i)
            elif(i>pivot):
                s2.append(i)
        return s+s1+s2