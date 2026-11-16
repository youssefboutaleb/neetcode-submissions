class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        for character in t:
            if character ==s[0]:
                s=s[1:]
                if s=="":
                    return True
        return False