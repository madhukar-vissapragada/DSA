class Solution:
    def decodeString(self, s: str) -> str:
        char_stack = []
        numb_stack = []

        number = ''
        for current in s:
            if current.isdigit():
                number += current 
            elif current == ']':
                result = ''
                while char_stack:
                    if char_stack[-1] == '[':
                        char_stack.pop()
                        result = int(numb_stack.pop()) * result
                        break
                    else:
                        result = char_stack.pop() + result
                char_stack.append(result)
            else:
                if number:
                    numb_stack.append(number)
                    number = ''
                char_stack.append(current)
        return ''.join(char_stack)