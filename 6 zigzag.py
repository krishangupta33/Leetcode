class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        l = len(s)
        result = [""] * numRows

        row = 0
        direction = 1  # 1 for downward, -1 for upward

        for char in s:
            result[row] += char
            if row == 0:
                direction = 1  # Change direction to downward when reaching the top row
            elif row == numRows - 1:
                direction = -1  # Change direction to upward when reaching the bottom row
            row += direction

        return ''.join(result)
    
f=Solution()
s="PAYPALISHIRING"
numRows=3
print(f.convert(s,numRows))