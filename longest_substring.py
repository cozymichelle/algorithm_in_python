"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If empty string, return 0
        if not s:
            return 0
        
        # If there is no repeating characters
        # return the length of the given string
        if len(set(s)) == len(s):
            return len(s)
        
        max_len = 0
        vocab = {}
        i = 0
        for j, char in enumerate(s):
            if char in vocab:
                i = max(vocab[char], i)
            max_len = max(max_len, j - i + 1)
            vocab[char] = j + 1
        
        return max_len