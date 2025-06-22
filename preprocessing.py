import pandas as pd
from surprise import Dataset, Reader

def load_data(file_path):
    df = pd.read_csv(file_path)
    reader = Reader(rating_scale = (1,5))
    data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)
    return data
