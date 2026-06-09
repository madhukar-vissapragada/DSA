class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        max_length = 0 
        i = j = 0 

        while j < len(s):
            if s[j] in hash_set:
                max_length = max(max_length, j - i)
                hash_set.discard(s[i])
                i += 1
            else:
                hash_set.add(s[j])
                j += 1
        return max_length


