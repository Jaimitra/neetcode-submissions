class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        i = 0
        max_count = -1
        while i < len(s):
            if s[i] not in seen:
                seen.add(s[i])
                max_count = max(max_count,(i-l)+1)
                i = i+1
            else:
                seen.remove(s[l])
                l = l+1
        return max(max_count,i-l)
        