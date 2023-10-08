class Solution:
    def isValid(self, s: str) -> bool:
        dict={"(":")","[":"]","{":"}"}
        for i in range(len(s)-1):
            if dict[s[i]]!=s[i+1]:
                return False
            else:
                return True
