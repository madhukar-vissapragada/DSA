class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for current in nums:
            if current in hash_map:
                hash_map[current] +=1 
            else:
                hash_map[current] = 1 
        
        freq = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))

        result = []
        count = 0 

        for key, value in freq.items():
            result.append(key)
            count += 1 

            if count == k:
                break 
        
        return result 

        