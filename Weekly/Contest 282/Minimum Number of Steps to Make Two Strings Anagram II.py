class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((collections.Counter(s)-collections.Counter(t)).values())+sum((collections.Counter(t)-collections.Counter(s)).values())   
