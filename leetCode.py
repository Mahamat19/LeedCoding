'''
*  LeetCode.py contain

'''
from typing import List
class LeetCode:
# 1. twoSum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
  def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):      # j starts from i+1 to in order to make to summation of two differents elts of nums.
                if j < len(nums):                 # to avoid being out of nums lenght (eg. 4 if len(nums)=3)
                    if nums[i] + nums[j] == target: # check if the summations of elts at indices i and j gives the target.
                        return [i,j]                # if so, return their corresponding indices.

# 9. Palindrome Number                   
"Given an integer x, return true if x is a palindrome, and false otherwise. Follow up: Could you solve it without converting the integer to a string?""
def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False #Because Negative numbers are not alindrome
        old_x = x #In order to compare it with it reversed

        "Were are going to compute successvily the euclidean division of x by 10"
        divisor_x = 0 #We initialise the divisor of x
        while x > 0: #We may set x!=0 but the negative case was already considered"
            reste = x % 10
            "Update divisor_x"
            divisor_x = divisor_x * 10 + reste
            x = x//10  #"consider integer division"
        if old_x == divisor_x: 
            return True
        else:
            return False