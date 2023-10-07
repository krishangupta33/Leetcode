class Solution:
    def longestPalindrome(self, s: str) -> str:
        #check if a palindrome or not
        def isPalindrome(s):
            return s==s[::-1]
        

        #generate all substrings
        substrings=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substrings.append(s[i:j])
        
        #sort the substrings by length
        substrings.sort(key=len,reverse=True)
        #check if palindrome or not
        palindromes=[]
        for i in substrings:
            if isPalindrome(i):
                return i
 
    



a=Solution()
s="vyzonecajxxdvswhftixmzgjbfoeilbnchqmdgoxfmkkkkcqguavfozmplhzgothrwpukzgkctdacbxefrzrmbgwwrrhpcvqwvgwgknyrtxxoligsqpbqoucltakbkywwssyodzydsjxeuvgiqqitkfkqnxsfflgbjvbxdrworsdkowtkgabnszgsmgytupybdclmmsmougfendwvzarfdfbixjnlxvevqfoohcgrrysofifdfulygrmkwpimduzzluojeqixdtcxhcqnfsdbunmhsglhiplgbhrqrrrprffjfradvbifxxhoqylkejyprxdtianietnjumltxywfowopghurofvwtxvaxtqnjbzwvljjwfmmlhixogwwyaoysvrpgfymyqjschhqcwvytkreirdxfapaomayebhkzxgmlthoxialmtnilfopvhhqlocytyrtpfmpgqakdbrsteurcpfvruicuxzukfpwjwgnuaaungwjwpfkuzxuciurvfpcruetsrbdkaqgpmfptrytycolqhhvpoflintmlaixohtlmgxzkhbeyamoapafxdrierktyvwcqhhcsjqymyfgprvsyoaywwgoxihlmmfwjjlvwzbjnqtxavxtwvforuhgpowofwyxtlmujnteinaitdxrpyjeklyqohxxfibvdarfjffrprrrqrhbglpihlgshmnubdsfnqchxctdxiqejoulzzudmipwkmrgylufdfifosyrrgchoofqvevxlnjxibfdfrazvwdnefguomsmmlcdbyputygmsgzsnbagktwokdsrowrdxbvjbglffsxnqkfktiqqigvuexjsdyzdoysswwykbkatlcuoqbpqsgiloxxtrynkgwgvwqvcphrrwwgbmrzrfexbcadtckgzkupwrhtogzhlpmzofvaugqckkkkmfxogdmqhcnblieofbjgzmxitfhwsvdxxjacenozyv"

print(a.longestPalindrome(s))