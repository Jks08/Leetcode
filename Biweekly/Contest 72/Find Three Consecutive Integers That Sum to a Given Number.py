class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        s=[]
        if(num%3==0):
            s.append(int(num/3 -1))
            s.append(int(num/3))
            s.append(int(num/3 +1))
        return s
        
