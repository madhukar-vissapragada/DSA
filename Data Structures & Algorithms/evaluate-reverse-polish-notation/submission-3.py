class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for current in range(len(tokens)):
            if tokens[current]  in ('+', '-', '*', '/'):
                first = stack.pop()
                second = stack.pop();

                result = None
                if tokens[current] == '+':
                    result = first + second 
                elif tokens[current] == '*':
                    result = first * second 
                elif tokens[current] == '-':
                    result = second - first 
                else:
                    result = int(second/first)
                
                stack.append(result)
            else:
                stack.append(int(tokens[current]))
        
        return stack[-1]
        