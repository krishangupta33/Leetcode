# Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

# Return the result table ordered by employee_id.

# The result format is in the following example.

 

# Example 1:

# Input:  
# Employees table:
# +-------------+-----------+------------+--------+
# | employee_id | name      | manager_id | salary |
# +-------------+-----------+------------+--------+
# | 3           | Mila      | 9          | 60301  |
# | 12          | Antonella | null       | 31000  |
# | 13          | Emery     | null       | 67084  |
# | 1           | Kalel     | 11         | 21241  |
# | 9           | Mikaela   | null       | 50937  |
# | 11          | Joziah    | 6          | 28485  |
# +-------------+-----------+------------+--------+

import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    all_employee_ids = employees['employee_id'].tolist()

    # Employees whose manager left the company i.e manager_id is not null and not in all_employee_ids
    manager_left = employees[employees['manager_id'].notnull() & ~employees['manager_id'].isin(all_employee_ids)]

    # Employee id where salary is less than 30000 and whose manager left the company
    result = manager_left[manager_left['salary'] < 30000][['employee_id']]
    #sort
    result.sort_values(by=['employee_id'], inplace=True)

    return result


    

