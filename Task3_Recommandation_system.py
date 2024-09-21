import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split

# Sample dataset: Users' ratings of different movies
# Rows represent users, columns represent movies
data = {
    'user_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'movie_id': [101, 102, 103, 101, 103, 104, 102, 103, 104],
    'rating': [5, 3, 4, 4, 5, 2, 3, 5, 4]
}

# Convert to a pandas DataFrame
ratings_df = pd.DataFrame(data)

# Pivot the data into a user-item matrix (rows: users, columns: movies)
user_item_matrix = ratings_df.pivot_table(index='user_id', columns='movie_id', values='rating')

# Fill NaN values with 0 to indicate no rating
user_item_matrix.fillna(0, inplace=True)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# Convert similarity matrix to a DataFrame
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to get top N similar users
def get_similar_users(user_id, similarity_matrix, n=2):
    similar_users = similarity_matrix[user_id].sort_values(ascending=False)[1:n+1]
    return similar_users.index.tolist()

# Function to recommend items for a user based on similar users
def recommend_items(user_id, user_item_matrix, similarity_matrix, top_n=2):
    # Find similar users
    similar_users = get_similar_users(user_id, similarity_matrix)
    
    # Get the items rated by similar users
    similar_users_ratings = user_item_matrix.loc[similar_users]
    
    # Find items not rated by the target user
    user_ratings = user_item_matrix.loc[user_id]
    unrated_items = user_ratings[user_ratings == 0].index
    
    # Average the ratings of similar users for the unrated items
    item_recommendations = similar_users_ratings[unrated_items].mean().sort_values(ascending=False)
    
    # Recommend top N items
    recommended_items = item_recommendations.head(top_n).index.tolist()
    
    return recommended_items

# Example usage: Recommend movies for user 1
user_id = 2
recommended_movies = recommend_items(user_id, user_item_matrix, user_similarity_df, top_n=2)

print(f"Recommended movies for User {user_id}: {recommended_movies}")
