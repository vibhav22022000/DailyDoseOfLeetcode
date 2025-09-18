class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s = str(x)
        # return s == s[::-1]

        #Negative Numbers
        if x < 0:
            return False
        
        if x % 10 == 0 and x!=0:
            return False
        
        reversed_half = 0

        while x > reversed_half:
            digit = x % 10
            reversed_half = (reversed_half * 10) + digit
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10