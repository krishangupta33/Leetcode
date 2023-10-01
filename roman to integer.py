# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.



"""
Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

def romanToInt(s: str):
    char = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M":1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD":400, "CM":900}

    list = []

    for i in range(len(s)):
        list.append(s[i])
 

    # joining IV, IX, XL, XC, CD, CM together
    for i in range(len(list)-1):
        if  list[i] == "I" and list[i+1] == "V":
            list[i] = "IV"
            list[i+1] = ""
        elif list[i] == "I" and list[i+1] == "X":
            list[i] = "IX"
            list[i+1] = ""
        elif list[i] == "X" and list[i+1] == "L":
            list[i] = "XL"
            list[i+1] = ""
        elif list[i] == "X" and list[i+1] == "C":
            list[i] = "XC"
            list[i+1] = ""
        elif list[i] == "C" and list[i+1] == "D":
            list[i] = "CD"
            list[i+1] = ""
        elif list[i] == "C" and list[i+1] == "M":
            list[i] = "CM"
            list[i+1] = ""

    list = [i for i in list if i != ""]
    
    return sum(char[i] for i in list)

print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("XV"))


