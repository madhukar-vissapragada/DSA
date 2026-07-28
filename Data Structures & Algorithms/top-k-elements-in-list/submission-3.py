class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for current in nums:
            if current in hash_map:
                hash_map[current] +=1 
            else:
                hash_map[current] = 1 
        
        sorted_data = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))

        result = []
        set_ = set()
        for current in sorted_data.items():
            if len(set_) == k:
                break
            result.append(current[0])
            set_.add(current[1])
    
        return result

        