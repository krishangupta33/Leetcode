
# Input: 
# Sales table:
# +---------+------------+------+----------+-------+
# | sale_id | product_id | year | quantity | price |
# +---------+------------+------+----------+-------+ 
# | 1       | 100        | 2008 | 10       | 5000  |
# | 2       | 100        | 2009 | 12       | 5000  |
# | 7       | 200        | 2011 | 15       | 9000  |
# +---------+------------+------+----------+-------+

# Output: 
# +------------+------------+----------+-------+
# | product_id | first_year | quantity | price |
# +------------+------------+----------+-------+ 
# | 100        | 2008       | 10       | 5000  |
# | 200        | 2011       | 15       | 9000  |
# +------------+------------+----------+-------+
# product_id is the primary key (column with unique values) of this table.
# Each row of this table indicates the product name of each product.

#Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
  ]

    sales.drop(columns="sale_id", inplace=True)

    sales["first_year"] = sales.groupby("product_id")["year"].transform("min")

    sales_filtered = sales[sales["year"] == sales["first_year"]]

    result = sales_filtered.iloc[:, [0, 4, 2, 3]]

    return result

