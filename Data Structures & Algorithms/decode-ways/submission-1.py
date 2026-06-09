class Solution:
    def numDecodings(self, s: str) -> int:
        number_to_letter = {}
        for i in range(26):
            number_to_letter[str(i + 1)] = chr(ord('A') + i)
        
        return self.solve(s, 0, 0, number_to_letter)


    def solve(self, s: str, start: int, end: int, number_to_letter: dict) -> int:
        if end > len(s) - 1:
            return 1 

        if s[start:end+1] not in number_to_letter:
            return 0 
        
        one_ele = self.solve(s, start + 1, end + 1, number_to_letter)
        two_ele = self.solve(s, start, end + 2, number_to_letter)

        result = one_ele + two_ele  
        return result 

