class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi,cur=-1,-1
        #arr[-1]=-1
        
        if len(arr)<3:
            if len(arr)==2:
                return [arr[-1],-1]
            else :
                return [-1]
        for i in range(len(arr)-2,-1,-1):
                maxi=max(maxi,arr[i+1],cur)
                cur=arr[i]
                arr[i]=maxi
        arr[-1]=-1
        return arr
