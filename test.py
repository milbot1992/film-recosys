import pandas as pd

movies_df = pd.read_csv('./Data/movies_metadata.csv')

# Find the index of the row where the title is 'Batman Begins'
index_batman_begins = movies_df.index[movies_df['title'] == 'The Thomas Crown Affair'].tolist()

# Print the row corresponding to 'Batman Begins'
if index_batman_begins:
    batman_begins_row = movies_df.iloc[index_batman_begins[0]]
    print(batman_begins_row)
else:
    print("Movie 'Batman Begins' not found in the DataFrame.")

