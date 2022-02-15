class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        c = Counter(beans)
        n = len(beans)
        tot = sum(beans)
        left_tot = 0  
        ans= float('inf')
        for k in sorted(c):
            n -= c[k]   
            tot -= k*c[k] 
            ans = min(ans, tot - n * k + left_tot)
            left_tot += k * c[k] 
        return ans
