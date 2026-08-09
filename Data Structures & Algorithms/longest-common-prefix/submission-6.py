class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        for i in strs:
            if len(i) < min_len:
                min_len = len(i)
        
        i = 0
        while i < min_len:
            for j in strs[1:]:
                if j[i] != strs[0][i]:
                    return j[:i]
            i = i+1

        return strs[0][:i]

            
        

        