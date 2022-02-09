class Bitset:
    def __init__(self, size: int):
        self.flipflag = 0 
        self.his = {}
        self.cnt = 0
        self.data = [ 0 for _ in range(size) ]
        self.dataflip = [ 1 for _ in range(size) ]
        self.n = size
        return None

    def fix(self, idx: int) -> None:
        if self.flipflag:
            if self.dataflip[idx] == 0:
                self.dataflip[idx] = 1
                self.data[idx] = 0
                self.cnt+=1
        else:
            if  self.data[idx] == 0:
                self.data[idx] = 1
                self.dataflip[idx] = 0
                self.cnt+=1

    def unfix(self, idx: int) -> None:
        
        if self.flipflag:
            if self.dataflip[idx] == 1:
                self.dataflip[idx] = 0
                self.data[idx] = 1
                self.cnt-=1
        else:
            if  self.data[idx] == 1:
                self.data[idx] = 0
                self.dataflip[idx] = 1
                self.cnt-=1
      
    
    def flip(self) -> None:
        self.cnt = self.n - self.cnt
        self.flipflag = 1 - self.flipflag

    def all(self) -> bool:
        return self.cnt == self.n
        
    def one(self) -> bool:
        return self.cnt > 0
        
    def count(self) -> int:
        return self.cnt 
        
    def toString(self) -> str:
        if self.flipflag:
            return ''.join(map(str, self.dataflip))
        return ''.join(map(str, self.data))