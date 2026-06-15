class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.solve(s, 0, len(s)-1, [], result)
        return result

    
    @staticmethod
    def is_palindrome(s: str):
        start = 0 
        end = len(s) - 1 

        while start <= end:
            if s[start] != s[end]:
                return False 
            start += 1 
            end -= 1
        return True

    def solve(self, s: str, start: int, end: int, current_palindrome: List[str], result: List[List[str]]):
        if start == len(s):
            result.append(current_palindrome.copy())
            return 
        
        for index in range(start, end+1):
            if Solution.is_palindrome(s[start:index+1]):
                current_palindrome.append(s[start:index+1])
                self.solve(s, index + 1, end, current_palindrome, result)
                current_palindrome.pop()
        
        
            


        