class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # i = 0
        # j = 1
        # s1 = nums[0]
        # min_len = float('inf')
        # while i < len(nums) and j < len(nums):
        #     if s1>=target:
        #         min_len = min(min_len,(j-i))
        #         s1 = s1 - nums[i]
        #         i = i+1
        #     else:
        #         s1 = s1 + nums[j]
        #         j = j+1
        i = 0 
        j = 0
        s1 = 0
        min_len = float('inf')
        for i in range(len(nums)):
            s1 = s1 + nums[i]
            if s1>=target:
                while s1>=target:
                    min_len = min(min_len,(i-j+1))
                    s1 = s1-nums[j]
                    j = j + 1
            # else:
            #     i = i+1
        return min_len if min_len != float('inf') else 0

        