class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        start = end = 0

        def isPalindrome(l,r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return l+1, r-1
        
        for i in range(len(s)):
            for a,b in (isPalindrome(i,i), isPalindrome(i,i+1)):
                if b - a > end - start:
                    start,end = a,b
        
        return s[start:end + 1]


        
        