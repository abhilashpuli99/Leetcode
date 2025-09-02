# Last updated: 9/2/2025, 1:43:41 PM
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1  # Start with a carry since we're adding one
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0  # Set current digit to 0 and carry over
                carry = 1
            else:
                carry = 0  # No carry is needed, we're done
                break
        
        if carry:
            digits.insert(0, 1)  # Insert 1 at the beginning if there's still a carry

        return digits
        