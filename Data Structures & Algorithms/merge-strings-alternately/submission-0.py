class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        size = min(m,n)
        idx1 = 0
        s = ""
        while idx1<size:
            s = s + word1[idx1]+word2[idx1]
            idx1+=1

        if idx1<m:
            s = s+word1[idx1:]
        if idx1<n:
            s=s+word2[idx1:]      
        return s