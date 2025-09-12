# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        can = None
        cnt = 0

        for i in nums:
            if cnt == 0:
                can = i
                cnt = 1
            elif can == i:
                cnt += 1
            else:
                cnt -= 1

        return can
