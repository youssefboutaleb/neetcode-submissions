class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans =nums
        k=0
        for num in nums :
            if num !=val:
                ans[k]=num
                k+=1
        nums = ans
        return k