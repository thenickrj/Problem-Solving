# Monotonic Array


"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].  An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Return true if and only if the given array nums is monotonic.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
Example 4:

Input: nums = [1,2,4,5]
Output: true
Example 5:

Input: nums = [1,1,1]
Output: true


PS: Monotonic means either entirely non-increasing, or entirely non-decreasing.
Source: LeetCode

"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]<=nums[len(nums)-1]:
            for i in range(0,len(nums)-1):
                if nums[i]>nums[i+1]:
                    return False            
        if nums[0]>=nums[len(nums)-1]:
            for i in range(0,len(nums)-1):
                if nums[i]<nums[i+1]:
                    return False
            

        return True    
        
