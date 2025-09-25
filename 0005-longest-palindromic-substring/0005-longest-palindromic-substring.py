class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        
        start = end = 0

        def isPalindrome(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(len(s)):
            for a,b in (isPalindrome(i,i), isPalindrome(i,i+1)):
                if b - a > end - start:
                    start = a
                    end = b
            
        return s[start:end+1]
        