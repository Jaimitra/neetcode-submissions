class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l<r:
            if not s[r].isalnum():
                r=r-1
                continue
            elif not s[l].isalnum():
                l=l+1
                continue
            else:
                if s[r].lower()!=s[l].lower():
                    return False
                r=r-1
                l=l+1
        return True
