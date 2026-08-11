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
        while i < len(s2)-k+1:
            a = {}
            for j in range(i,i+k):
                if s2[j] not in a and s2[j] in s1:
                    a[s2[j]] = 1
                elif s2[j] in a:
                    a[s2[j]] += 1
            print(a,s1_key)
            if a == s1_key:
                return True
            i = i+1
        return False

        