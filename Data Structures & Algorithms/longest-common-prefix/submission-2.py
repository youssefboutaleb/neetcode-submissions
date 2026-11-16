class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=strs[0]

        for s in strs[1:]:
            ans=ans[:len(s)]
            if s=="":
                return ""
            for i in range(len(ans)):
                if ans[i]==s[i]:
                    pass
                else :
                    ans=ans[:i]
                    break
            if ans=="":
                return ""
        return ans
