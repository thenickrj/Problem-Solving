# Median of Two sorted Arrays


"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.


Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Source: LeetCode
"""
def findMedianSortedArrays(nums1,nums2):
    num3=nums1+nums2
    num3=sorted(num3)
    n=len(num3)
    if n%2==1:
        median=num3[len(num3)//2]
    else:
        median=(num3[len(num3)//2]+num3[(len(num3)//2)-1])/2
    return median
