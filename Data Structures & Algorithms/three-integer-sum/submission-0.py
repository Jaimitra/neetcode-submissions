class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = set()
        for i in range(0,len(nums)):
            seen = set()
            for j in range(i+1,len(nums)):
                if -(nums[i]+nums[j])  in seen:
                    a.add(tuple(sorted([nums[i],nums[j],-(nums[i]+nums[j]) ]) ))
                else:
                    seen.add(nums[j])
        return list(map(list,a))
        