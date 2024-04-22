import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import logging

def user_based_collaborative_filtering(collab_df):
    """
    Perform user-based collaborative filtering.

    Args:
        collab_df (pd.DataFrame): DataFrame containing relevant fields from movies_df, ratings_df, links_df

    Returns:
        tuple: A tuple containing two functions:
            - users_choice: Function to retrieve top movie choices for a given user.
            - common: Function to recommend movies for a given user based on similar users' preferences.
    """
    logging.info("Performing user-based collaborative filtering...")

    logging.info("Pivoting users table...")
    users_pivot = collab_df.pivot_table(index=["userId"], columns=["title"], values="rating")
    users_pivot.fillna(0, inplace=True)

    def users_choice(user_id):
        """
        Retrieve top movie choices for a given user.

        Args:
            user_id (int): ID of the user.

        Returns:
            pd.DataFrame: DataFrame containing top movie choices for the user.
        """
        unique_user_ids = collab_df["userId"].unique()
        user_data = collab_df[collab_df["userId"] == user_id].sort_values(["rating"], ascending=False)[0:5]
        user_data = user_data.loc[:, ["title", "release_date", "rating", "new_full_image_url"]]
        # Rename the column 'new_full_image_url' to 'poster_url'
        user_data.rename(columns={"new_full_image_url": "poster_url"}, inplace=True)
        return user_data

    def user_based(user_id):
        """
        Get similar users based on user ID.

        Args:
            user_id (int): ID of the user.

        Returns:
            list: List of user IDs similar to the input user.
        """
        if user_id not in collab_df["userId"].values:
            return []
        
        index = np.where(users_pivot.index == user_id)[0][0]
        similarity = cosine_similarity(users_pivot)
        similar_users = list(enumerate(similarity[index]))
        similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)[0:5]
        
        user_rec = []
        for i in similar_users:
            data = collab_df[collab_df["userId"] == users_pivot.index[i[0]]]
            user_rec.extend(list(data.drop_duplicates("userId")["userId"].values))
            
        return user_rec

    def common(user_id):
        """
        Recommend movies for a given user based on similar users' preferences.

        Args:
            user_id (int): ID of the user.

        Returns:
            list: List of recommended movies for the user.
        """
        x = collab_df[collab_df["userId"] == user_id]
        recommend_films = []
        user = user_based(user_id)

        for i in user:
            y = collab_df[(collab_df["userId"] == i)]
            films = y.loc[~y["title"].isin(x["title"]), :]
            films = films.sort_values(["rating"], ascending=False)[0:5]

            for index, row in films.iterrows():
                film_entry = {
                    "title": row["title"],
                    "vote_average": row["vote_average"],
                    "poster_url": row["new_full_image_url"],
                }
                recommend_films.append(film_entry)
            
        return recommend_films[0:5]
    
    logging.info("User-based collaborative filtering completed.")

    return users_choice, common
