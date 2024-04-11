import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def user_based_collaborative_filtering(collab_df):

    def get_image_url(new_poster_path, size='w500'):
            base_url = "https://image.tmdb.org/t/p/"
            new_image_url = f"{base_url}{size}{new_poster_path}"
            return new_image_url
        
    # Generate new_image_url for each movie and add it to the DataFrame
    collab_df['new_image_url'] = collab_df.apply(lambda row: get_image_url(row['new_poster_path']), axis=1)
    
    users_pivot = collab_df.pivot_table(index=["userId"], columns=["title"], values="rating")

    users_pivot.fillna(0, inplace=True)

    def users_choice(user_id):
        print('>>>>>collab_df: ', collab_df)
        print('>>>>>user_id: ', user_id)
        unique_user_ids = collab_df["userId"].unique()
        print("Unique user IDs:", unique_user_ids)
        user_data = collab_df[collab_df["userId"] == user_id].sort_values(["rating"], ascending=False)[0:5]
        print('>>>>>user_data: ', user_data)
        user_data = user_data.loc[:, ["title", "release_date", "rating", "new_image_url"]]
        return user_data

    def user_based(user_id):
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
                    "poster_url": row["new_image_url"],
                }
                recommend_films.append(film_entry)
            
        return recommend_films[0:5]

    return users_choice, common