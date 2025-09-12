# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        strs.sort()
        
        start = strs[0]
        last = strs[-1]

        for i in range(min(len(start), len(last))):
            if start[i] != last[i]:
                return result
            result+=start[i]
        return result