class Solution:
    def partition(self, s: str) -> List[List[str]]:
         result = []
         self.solve(s, 0, [], result)
         return result 
    

    def solve(self, s: str, current_index: int, current_config: List[str], result: List[List[str]]):
        def is_palindrome(s: str):
            i = 0 
            j = len(s) - 1 

            while i <= j:
                if s[i] != s[j]:
                    return False 
                
                i += 1 
                j -= 1 
            
            return True 
        
        if current_index == len(s):
            result.append(current_config.copy())
            return 
        
        for index in range(current_index, len(s)):
            left_part = s[current_index:index+1]
            if is_palindrome(left_part):
                current_config.append(left_part)
                self.solve(s, index + 1, current_config, result)
                current_config.pop()
        

        