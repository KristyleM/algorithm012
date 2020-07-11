class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = 1
        for i in range(len(digits), 0, -1):
            i = i - 1
            digits[i] = digits[i] + temp
            temp = 0
            if digits[i] == 10:
                digits[i] = 0
                temp = 1

        if temp:
            digits.insert(0, temp)

        return digits

