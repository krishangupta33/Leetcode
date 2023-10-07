class Solution:
    def reverse(self, x: int) -> int:
        #storing s string
        s=str(x)
        #checking if negative
        if s[0]=="-":
            #removing negative sign
            s=s[1:]
            #reversing the string
            s=s[::-1]
            #adding negative sign
            s="-"+s
        else:
            #reversing the string
            s=s[::-1]
        
        #converting to int
        s=int(s)
        #checking if in range
        if s>=-2**31 and s<=(2**31)-1:
            return s
        else:
            return 0