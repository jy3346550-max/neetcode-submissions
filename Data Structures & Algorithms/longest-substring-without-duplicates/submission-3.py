class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strMap = {}
        left = 0
        result = 0

        for c in range(len(s)):
            if s[c] in strMap:
                left = max(strMap[s[c]] + 1, left)
            strMap[s[c]] = c
            result = max(result, c - left + 1)
        return result