# Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

# Return the result table ordered by id in ascending order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Seat table:
# +----+---------+
# | id | student |
# +----+---------+
# | 1  | Abbot   |
# | 2  | Doris   |
# | 3  | Emerson |
# | 4  | Green   |
# | 5  | Jeames  |
# +----+---------+
# Output: 
# +----+---------+
# | id | student |
# +----+---------+
# | 1  | Doris   |
# | 2  | Abbot   |
# | 3  | Green   |
# | 4  | Emerson |
# | 5  | Jeames  |
# +----+---------+

import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    dummy='dummy'
    for i in range(0, len(seat)-1, 2):
        dummy = seat.loc[i, 'student']
        
        seat.loc[i, 'student'] = seat.loc[i+1, 'student']
        
        seat.loc[i+1, 'student'] = dummy

    return seat