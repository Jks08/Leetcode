class Solution:
    def minimumSum(self, num: int) -> int:
        nums1=[int(x) for x in str(num)]
        nums1.sort()
        a=0
        b=0
        for i in range(len(nums1)):
            if(i%2!=0):
                a=a*10+nums1[i]
            else:
                b=b*10+nums1[i]
        return a+b
        