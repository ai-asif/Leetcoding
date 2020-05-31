' Rightmost digit is always added.
' So sum is initialized to rightmost digit to decrease complexity
roman_dict = {"I": 1,
                     "V" : 5,
                     "X" : 10,
                     "L" : 50,
                     "C" : 100,
                     "D" : 500,
                     "M" : 1000}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        num = roman_dict.get(s[l - 1])
        
        
        for i in range(l - 1):
                if roman_dict.get(s[i]) < roman_dict.get(s[i + 1]):
                    num = num - roman_dict.get(s[i])
                else:
                    num = num + roman_dict.get(s[i])
        return num
        