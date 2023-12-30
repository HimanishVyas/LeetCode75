# ---- Array ----

'''
Given an array of integer nums and an integer target, return indices of the two numbers such that they add up to the target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# class Solution(object):

# ------this passed 52/61 test (this failed in [3,3])  
def twoSum(nums, target):
        for i in nums:
            j = target - i
            if j != i and j in nums:
                print(j)
                a = [nums.index(i), nums.index(j)]
                print(a)
                return a

# ----- This is running solution passes every test case 
def twoSum(nums, target):
    for cur in range(len(nums)): # this  will go with index number of list / array
        for x in range(cur + 1, len(nums)): # ths will start from index one / 1
            if nums[x] == target - nums[cur]: 
                print([cur, x])
                return [cur, x]
            


nums = [5, 3, 6, 2]
target = 7
twoSum(nums, target)
