class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def isNotZero(x: int) -> bool:
            return '0' not in str(x)
        
        for a in range(1,n):
            b = n - a

            if isNotZero(a) and isNotZero(b):
                return [a,b]
        