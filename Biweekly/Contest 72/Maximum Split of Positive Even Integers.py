class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2: return []
        value = int(sqrt(finalSum))
        ans = [2 * i for i in range(1, value)]    
        diff = finalSum - sum(ans)
        if ans and diff <= ans[-1]:
            return ans[:-1] + [diff + ans[-1]]
        else:    
            return ans + [diff]
