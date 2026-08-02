class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        self.prices.append(price)
        count = 0 
        for index in range(len(self.prices)-1, -1, -1):
            if index > 0:
                if self.prices[index-1] > price:
                    count += 1 
                    break
                else:
                    count += 1 
            else:
                count += 1 
                break 
        
        return count
            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)