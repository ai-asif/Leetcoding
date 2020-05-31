class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        my_dict = {}
        for i in range(n):
            complement = target - nums[i]
            if complement in my_dict:
                return [i, my_dict.get(complement)]    
            my_dict[nums[i]] = i
        