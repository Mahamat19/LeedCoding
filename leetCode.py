'''
*  LeetCode.py contain

'''
from typing import List
class LeetCode:
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
  def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):      # j starts from i+1 to in order to make to summation of two differents elts of nums.
                if j < len(nums):                 # to avoid being out of nums lenght (eg. 4 if len(nums)=3)
                    if nums[i] + nums[j] == target: # check if the summations of elts at indices i and j gives the target.
                        return [i,j]                # if so, return their corresponding indices.