class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        data = []
        nums.sort()
        count = 0
        cur = nums[0]
        for i in range(n):
            if nums[i] == cur:
                count+=1
            else:
                if count>n//3:
                    data.append(cur)
                count = 1
                cur = nums[i]
        if count>n//3:
            data.append(cur)
        return data
        