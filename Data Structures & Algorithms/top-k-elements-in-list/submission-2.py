class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for current in nums:
            if current in hash_map:
                hash_map[current] +=1 
            else:
                hash_map[current] = 1 
        
        sorted_data = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))

        sorted_data = list(sorted_data.items())[:2]

        result = []
        for current in sorted_data:
            result.append(current[0])
         
        return result

        