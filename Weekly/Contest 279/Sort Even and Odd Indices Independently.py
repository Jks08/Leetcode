class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums1=[]
        nums2=[]
        nums3=[]
        for i in range(len(nums)):
            if(i%2==0):
                nums1.append(nums[i])
            else:
                nums2.append(nums[i])
        nums1.sort()
        nums2.sort(reverse=True)
        x=0
        y=0
        for i in range(len(nums)):
            if(i&1):
                nums3.append(nums2[y])
                y+=1
            else:
                nums3.append(nums1[x])
                x+=1
        return nums3
        
