import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:

    #replacing null values in referee_id column with 9999
    customer['referee_id'] = customer['referee_id'].fillna(9999)


    return customer.loc[customer['referee_id'] != 2, ['name']]