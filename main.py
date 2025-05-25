from leetCode import LeetCode

if __name__=="__main__":
    leet_obj = LeetCode()
    nums, target = [2,7,11,15], 9
    print(leet_obj.twoSum(nums,target))

    x1 = 121
    print(leet_obj.isPalindrome(x1))

    x2 = -121
    print(leet_obj.isPalindrome(x2))
    x3 = 10
    print(leet_obj.isPalindrome(x3))



