import bisect 

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic = {v: i for i, v in enumerate(nums2)}
        lst = [dic[v] for v in nums1] 
        res = 0
        stack = []
        l = len(lst)
        for i, v in enumerate(lst):
            idx = bisect.bisect(stack, v)
            res += idx * (l - v - (i - idx) - 1)
            bisect.insort(stack, v)
        return res
