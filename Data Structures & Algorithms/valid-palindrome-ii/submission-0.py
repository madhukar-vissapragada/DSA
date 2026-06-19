class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = j = 0 

        while j < len(s):
            a = s[:i]
            b = s[i+1:]
            c = a + b 


            if self.is_palindrome(c):
                return True 
            else:
                i += 1
            
            j += 1
        
        return False 
    

    def is_palindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1 

        while i <= j:
            if s[i] != s[j]:
                return False 
            
            i += 1 
            j -= 1 

        return True 

        