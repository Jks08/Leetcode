class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        for i,n in enumerate(nums):
            d[math.gcd(n,k)] += 1
        ans = 0
        
        for a in d:
            for b in d:
                if b >= a and a*b%k == 0:
                    if a != b:
                        ans += d[a]*d[b]
                    else:
                        ans += d[a]*(d[a]-1)//2
        return ans
