class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        suffix = []
        n = len(nums)
        i = 0
        j = n-1
        pre_s = 1
        suf_s = 1
        while i < len(nums) and j>=0:
            pre_s *= nums[i]
            suf_s *= nums[j]
            prefix.append(pre_s)
            suffix.append(suf_s)
            i=i+1
            j=j-1
        suffix[:] = suffix[::-1]
        for i in range(n):
            if i == 0:
                res.append(suffix[i+1])
            elif i == n-1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*suffix[i+1])
        return res
        