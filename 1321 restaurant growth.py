# You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

# Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.

# Return the result table ordered by visited_on in ascending order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Customer table:
# +-------------+--------------+--------------+-------------+
# | customer_id | name         | visited_on   | amount      |
# +-------------+--------------+--------------+-------------+
# | 1           | Jhon         | 2019-01-01   | 100         |
# | 2           | Daniel       | 2019-01-02   | 110         |
# | 3           | Jade         | 2019-01-03   | 120         |
# | 4           | Khaled       | 2019-01-04   | 130         |
# | 5           | Winston      | 2019-01-05   | 110         | 
# | 6           | Elvis        | 2019-01-06   | 140         | 
# | 7           | Anna         | 2019-01-07   | 150         |
# | 8           | Maria        | 2019-01-08   | 80          |
# | 9           | Jaze         | 2019-01-09   | 110         | 
# | 1           | Jhon         | 2019-01-10   | 130         | 
# | 3           | Jade         | 2019-01-10   | 150         | 
# +-------------+--------------+--------------+-------------+
# Output: 
# +--------------+--------------+----------------+
# | visited_on   | amount       | average_amount |
# +--------------+--------------+----------------+
# | 2019-01-07   | 860          | 122.86         |
# | 2019-01-08   | 840          | 120            |
# | 2019-01-09   | 840          | 120            |
# | 2019-01-10   | 1000         | 142.86         |
# +--------------+--------------+----------------+



import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    #sum amount column group by visited_on
    sumdf=customer.groupby('visited_on').sum()

    #rename amount column to sum_amount
    sumdf.rename(columns={'amount':'sum_amount'}, inplace=True)

    #reset index
    sumdf.reset_index(inplace=True)

    #rolling 7 days sum
    sumdf['amount']=sumdf['sum_amount'].rolling(7).sum()

    #rolling 7 days average till 2 decimal
    sumdf['average_amount']=round(sumdf['amount']/7, 2)

    #drop first 6 rows
    sumdf.drop(range(6), inplace=True)



    #return three columns date, rolling_sum, average_amount

    return sumdf[['visited_on', 'amount', 'average_amount']]
    
    
