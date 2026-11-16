class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums :
            count[num] = 1 + count.get(num,0)
        return [num for num,count in sorted(list(count.items()),reverse=True, key=lambda x : x[1])][:k]