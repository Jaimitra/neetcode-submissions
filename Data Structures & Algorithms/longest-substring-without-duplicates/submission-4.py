class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        cur = 0
        max_ele = -1
        while i < len(s):
            if s[i] not in seen:
                seen.add(s[i])
                max_ele = max(max_ele,(i-cur)+1)
                i = i+1
            else:
                seen.remove(s[cur])
                cur = cur + 1
        # while i < len(s):
        #     if s[i] not in seen:
        #         seen.add(s[i])
        #         max_ele = max(max_ele,(i-cur)+1)
        #         i = i+1
        #     else:
        #         while s[i] in seen:
        #             seen.remove(s[cur])
        #             cur = cur + 1

                
        return max(max_ele,(i-cur))

        
        