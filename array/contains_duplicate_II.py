# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for i, v in enumerate(nums):
            if v in seen.keys():
                seen[v].append(i)
            else:
                seen[v] = [i]
        print(seen)
        for v in seen.values():
            if len(v) > 1:
                for j in range(len(v)-1):
                    initial = v[j]
                    for a in range(j+1, len(v)):
                        if abs(initial - v[a]) <= k:
                            return True
        return False

# TC: O(n) + O(n) * O(n) * O(n) = O(2n^3) -> O(n^3) # wrong; O(n^2) right;
