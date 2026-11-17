class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=dict()
        for s in strs :
            groups.setdefault("".join(sorted(s)), []).append(s)
        
        anagrams=[]
        for g in groups:
            anagrams.append(groups[g])
        return anagrams