from recommend import get_recommendations

if __name__ =="__main__":
    user_id = 1
    recommendations = get_recommendations(user_id)

    if recommendations:
        print(f"Top Recommendations for user {user_id}: {recommendations}")
    else:
        print(f"No recommedations available for user {user_id}")