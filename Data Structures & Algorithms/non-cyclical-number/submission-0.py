class Solution:
    def isHappy(self, n: int) -> bool:
        return self.solve(n, set()) 

    def solve(self, n: int, hash_set: set) -> bool:
        if n == 1:
            return True 

        if n in hash_set:
            return False 
        
        sum_ = 0
        while n > 0:
            sum_ += n % 10
            n = n//10 
        
        hash_set.add(sum_)
        return self.solve(sum_, hash_set)



        