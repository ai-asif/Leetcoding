class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        window_size = [0]
        win_len = 0
        
        start = False

        for num in nums:
            if num == 1:
                if start == False:
                    start = True
                win_len = win_len + 1

            else:
                if start == True:
                    start = False
                    window_size.append(win_len)
                    win_len = 0
        window_size.append(win_len)               
        return max(window_size)