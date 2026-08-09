class Solution:
    def merge(self,nums,start,mid,end):
        idx1 = start
        idx2 = mid+1
        temp = []
        while idx1<=mid and idx2<=end:
            if nums[idx1]>=nums[idx2]:
                temp.append(nums[idx2])
                idx2+=1
            else:
                temp.append(nums[idx1])
                idx1+=1   
        while idx1<=mid:
            temp.append(nums[idx1])
            idx1+=1 
        while idx2<=end:
            temp.append(nums[idx2])
            idx2+=1   

        for k in range(len(temp)):
            nums[start + k] = temp[k]

    def merge_sort(self,nums,start,end):
        if start>=end:
            return
        mid = (start+end) // 2
        self.merge_sort(nums,start,mid)
        self.merge_sort(nums,mid+1,end)
        self.merge(nums,start,mid,end)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums,0,len(nums)-1)
        return nums
        