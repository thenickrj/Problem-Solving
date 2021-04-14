# Valid Palindrome

"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.


Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        d = ""
        for i in s:
            if i.isalnum() == True:
                d += i
        if len(d) == 1:
            return True
        if d[::-1].lower() == d.lower():
            return True
        return False

