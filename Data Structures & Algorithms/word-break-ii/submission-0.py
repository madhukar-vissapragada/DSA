class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        self.solve(s, set(wordDict), 0, [], result)
        return result 
    
    def solve(self, s: str, word_dict: set, current_index: int, current_sentence: List[str], result: List[List[int]]):
        if current_index == len(s):
            result.append(' '.join(current_sentence).strip())
            return 
        
        for index in range(current_index, len(s)):
            left = s[current_index: index + 1]
            right = s[index + 1 : len(s)]
            if left in word_dict:
                current_sentence.append(left)
                self.solve(s, word_dict, index + 1, current_sentence, result)
                current_sentence.pop()


