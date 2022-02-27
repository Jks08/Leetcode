class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        for i in words:
            if(len(i)>1):
                if(i[:len(pref)]==pref):
                    count+=1
            else:
                if((i[:len(pref)])==pref):
                    count+=1
        return count
