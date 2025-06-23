from preprocessing import load_ratings
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def get_recommendations(user_id, data_path = "ecommerce_data.csv", top_n = 5):
    user_item_matrix = load_ratings(data_path)
    if user_item_matrix is None or user_id not in user_item_matrix.index:
        return []

    # compute user-user similarity
    user_similarity = cosine_similarity(user_item_matrix)
    similarity_df = pd.DataFrame(user_similarity, index = user_item_matrix.index, columns = user_item_matrix.index)

    #get similar users
    similar_users = similarity_df[user_id].sort_values(ascending = False)[1:6]

    # aggregate ratings from similar users
    recommendations = pd.Series(dtype = 'float64')
    for sim_user_id in similar_users.index:
        sim_user_ratings = user_item_matrix.loc[sim_user_id]
        recommendations = recommendations.add(sim_user_ratings, fill_value = 0)

    #Remove already rated items
    already_rated = user_item_matrix.loc[user_id]
    recommendations[already_rated > 0] = 0
    recommendations = recommendations.sort_values(ascending = False).head(top_n)

    return list(recommendations.index)
