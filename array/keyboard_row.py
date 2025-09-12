# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]

# Output: ["Alaska","Dad"]

# Explanation:

# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

# Example 2:

# Input: words = ["omk"]

# Output: []

# Example 3:

# Input: words = ["adsdf","sfd"]

# Output: ["adsdf","sfd"]


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first_row = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        second_row = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
        third_row = ["z", "x", "c", "v", "b", "n", "m"]

        res = []
        from_row = 0
        current_word = ""

        for word in words:
            for char in word:
                if from_row == 0:
                    if char.lower() in first_row:
                        from_row = 1
                        current_word += char
                    elif char.lower() in second_row:
                        from_row = 2
                        current_word += char
                    else:
                        from_row = 3
                        current_word += char
                else:
                    if from_row == 1 and char.lower() not in first_row:
                        from_row = 0
                        current_word = ""
                        break
                    elif from_row == 2 and char.lower() not in second_row:
                        from_row = 0
                        current_word = ""
                        break
                    elif from_row == 3 and char.lower() not in third_row:
                        from_row = 0
                        current_word = ""
                        break
                    else:
                        current_word += char
            if current_word:
                res.append(current_word)
            current_word = ""
            from_row = 0

        return res