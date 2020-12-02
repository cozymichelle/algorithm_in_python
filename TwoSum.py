"""
Two Sum Problem
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) == 2:
            return [0, 1]
        
        lookup = {}        
        for i, num in enumerate(nums):
            candidate = target - num
            if candidate in lookup:
                return [lookup[candidate], i]
            lookup[num] = i
