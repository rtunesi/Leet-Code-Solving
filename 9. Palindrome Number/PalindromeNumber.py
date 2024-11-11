# 9. Palindrome Number - Leetcode problem

value1 = 121
value2 = -121
value3 = 30

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

# Testing Environment
value3 = str(value3)
if value3 == value3[::-1]:
    print(True)
else:
    print(False)