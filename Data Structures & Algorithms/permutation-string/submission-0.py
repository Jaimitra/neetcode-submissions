class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        k = len(s1)
        a = sorted(s1)
        while i < len(s2)-k+1:
            if a == sorted(s2[i:k+i]):
                return True
            i = i+1
        return False

        