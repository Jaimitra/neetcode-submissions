class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        count = 1
        max_count = -float('inf')
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                count+=1
            else:
                max_count = count if count>max_count else max_count
                count = 1
        return max_count if max_count>count else count