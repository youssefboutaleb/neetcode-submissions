class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        alphabet=[0 for _ in range(26)]
        for i in range(len(s)):
            alphabet[ord(s[i])-97]+=1
            alphabet[ord(t[i])-97]-=1
        return alphabet==[0 for _ in range(26)]