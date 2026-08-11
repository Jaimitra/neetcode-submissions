class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_key = {}
        for i in s1:
            if i not in s1_key:
                s1_key[i] = 1
            else:
                s1_key[i] += 1
        i = 0
        k = len(s1)
        a = sorted(s1)
        while i < len(s2)-k+1:
            if a == sorted(s2[i:k+i]):
                return True
            i = i+1
        return False

        