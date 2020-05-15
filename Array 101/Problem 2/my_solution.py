class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        evens = 0
        
        for num in nums:
            num_length = 0
            while True:
                num_length = num_length + 1
                if  num % 10 == num:
                    break
                else:
                    num = num / 10
                
                
            if num_length % 2 == 0:
                evens = evens + 1
        
        return evens
    
