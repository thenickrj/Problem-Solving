# Reverse Integer

"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
then return 0.

Input: x = 123
Output: 321

Input: x = -123
Output: -321

"""


def reverse(x):
    reverseInteger = int(str(abs(x))[::-1])
       
    if(reverseInteger.bit_length()>31):
        return 0

    if x<0:
        return -1*reverseInteger
    else:
        return reverseInteger

print(reverse(-123))        