class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        slist = sorted(s)[::-1]
        cs = [[a,b] for a,b in Counter(slist).items()]
        ans = ''
        count = 0
        
        while True:
            if not cs:
                break
            
            while cs and cs[0][1] > 0 and count < repeatLimit:
                ans += cs[0][0]
                cs[0][1] -= 1
                count += 1
            
            if cs[0][1] == 0:
                cs.pop(0)
                count = 0
                continue
            
            if count == repeatLimit:
                count = 0
                if len(cs) > 1:
                    ans += cs[1][0]
                    cs[1][1] -= 1
                    if cs[1][1] == 0:
                        cs.pop(1)
                else:
                    break
        return ans
