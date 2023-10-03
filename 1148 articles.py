import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df= views.loc[views['author_id']==views['viewer_id'],['author_id']]

    #change column name
    df.columns=['id']
    return df.drop_duplicates().sort_values(by='id',ascending=True)