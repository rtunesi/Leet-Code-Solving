# 1. Two Sum - Leetcode problem

# Steps to solve:
# 1. Identify Pairs: You need to check pairs of numbers in nums to see if their sum is equal to the target.
# 2. Return Indices: Instead of returning the numbers, you need to return their indices in the array.

nums = [1, 3, 6, 7, 11]
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]