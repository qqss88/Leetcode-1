#!/usr/bin/env python
# encoding: utf-8

"""
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12],
after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

@author: Jessie
@email: jessie.JNing@gmail.com
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for k in range(len(nums)):
            if nums[i] == 0:
                j = i
                while j < len(nums)-1:
                    nums[j] = nums[j+1]
                    j += 1
                nums[j] = 0
            else:
                i +=1




if __name__=="__main__":

    test = Solution()
    test.moveZeroes([0,1,0,3,12])