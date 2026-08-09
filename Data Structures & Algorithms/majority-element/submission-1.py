class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        max_count = -float('inf')
        count = 1
        prev = nums[0]
        cur = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i] == prev:
                count+=1
            else:
                max_count,cur = (count,nums[i-1]) if count > max_count else  (max_count,cur)
                prev = nums[i]
                count = 1
        return prev if count>max_count else cur

        