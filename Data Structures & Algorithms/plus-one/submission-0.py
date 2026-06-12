class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for index in range(len(digits) - 1, -1, -1):
            current = digits[index] + carry 
            if current > 9:
                digits[index] = 0
                carry = 1
            else:
                digits[index] = current
                carry = 0

        if carry:
            digits.insert(0, carry)

        return digits