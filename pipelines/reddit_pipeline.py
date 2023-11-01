from etls.reddit_etl import connect_reddit, extract_post,transform_data,load_data_to_csv
from utils.constants import CLIENT_ID,SECRET,OUTPUT_PATH
import pandas as pd

def reddit_pipeline(file_name:str, subreddit:str, time_filter='day',limit=None):
    #Connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    #extraction 
    posts = extract_post(instance,subreddit,time_filter,limit)
    post_df = pd.DataFrame(posts)
    #transformation 
    post_df = transform_data(post_df)
    #loading to csv
    filepath = f'{OUTPUT_PATH}/{file_name}.csv' 
    load_data_to_csv(post_df,filepath)

    return filepath
