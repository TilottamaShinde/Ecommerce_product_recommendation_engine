import pandas as pd

def load_ratings(file_path):

    """
    load and preprocess the user rating data.
    Return a user-item matrix(rows = users, columns = items)
    :param file_path:
    :return:
    """
    try:

        df = pd.read_csv(file_path)
        #Basic Checkes

        df.dropana(inplace = True)
        df = df[df['rating']>0] #Removes 0 or negative rating if any

        user_item_matrix = df.pivot_table(
            index = 'user_id',
            columns = 'item_id',
            values = 'rating'
        ).fillna(0)
        return user_item_matrix
    except Exception as e:
        print("Error loading or preprocessing data", e)
        return None
