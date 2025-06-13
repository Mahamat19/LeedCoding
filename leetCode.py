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
        
# 15. 3Sum
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.
def threeSum(self, nums: List[int]) -> List[List[int]]:
    Output = [] #Output list to be filed
    Set_ver = set()

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)): # The fact that j (resp. k) starts from i+1 (resp. j+1) means that i != j, i != k, and j != k 
                if nums[i] + nums[j] + nums[k] == 0:
                    sum_got_sorted = sorted([nums[i], nums[j], nums[k]])
                    sum_got_tuple = tuple(sum_got_sorted)
                    if sum_got_tuple not in Set_ver:
                        Set_ver.add(sum_got_tuple)
                        Output.append(sum_got_tuple)
                        
                            
                    
    return Output