class Solution:
    def merge(self, n1: List[int], m: int, n2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = 0
        idx2 = 0
        temp = []
        while idx1<m and idx2<n:
            if n1[idx1]>=n2[idx2]:
                temp.append(n2[idx2])
                idx2+=1
            else:
                temp.append(n1[idx1])
                idx1+=1
        while idx1<m:
            temp.append(n1[idx1])
            idx1+=1        

        while idx2<n:
            temp.append(n2[idx2])
            idx2+=1
        n1[:]=temp[:]
        
        