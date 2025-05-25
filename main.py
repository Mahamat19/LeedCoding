from leetCode import LeetCode

if __name__=="__main__":
    leet_obj = LeetCode()

    #twoSum
    nums, target = [2,7,11,15], 9
    print(leet_obj.twoSum(nums,target))

    #Palindrome Number
    x1 = 121
    print(leet_obj.isPalindrome(x1))

    x2 = -121
    print(leet_obj.isPalindrome(x2))
    x3 = 10
    print(leet_obj.isPalindrome(x3))

    #3Sum
    nums1 = [-1,0,1,2,-1,-4]
    print(leet_obj.isPalindrome(nums1))

    nums2 = [0,1,1]
    print(leet_obj.isPalindrome(nums2))

    nums3 = [0,0,0]
    print(leet_obj.isPalindrome(nums3))



