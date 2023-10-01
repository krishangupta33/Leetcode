class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()

        for i in range(len(words)):
            words[i]=words[i][::-1]

        joined=" ".join(words)
        return joined
    




classobject=Solution()

print(classobject.reverseWords("the sky is blue"))