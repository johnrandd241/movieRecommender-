import tkinter as tk
import pandas as pd

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
#Data
df = pd.read_csv('file.tsv', sep = '\t', names = column_names)
titles = pd.read_csv('Movie_Id_Titles.csv')
data = pd.merge(df, titles, on = 'item_id')

# creating dataframe with 'rating' count values
ratings = pd.DataFrame(data.groupby('title')['rating'].mean()) 
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

# Sorting values according to 
# the 'num of rating column'
moviemat = data.pivot_table(index ='user_id', columns ='title', values ='rating')
#--------------------------------------------------
print("Welcome to John's movie recommender app!\n")
inp = ' '
while inp != 'E':
    inp = input("Enter movie, enter E to exit\n")
    if inp == 'E':
        print('Goodbye!')
    else:
        inp_user_ratings = moviemat[inp]
        similar_to_inp = moviemat.corrwith(inp_user_ratings)
        corr_inp = pd.DataFrame(similar_to_inp, columns =['Correlation'])
        corr_inp.dropna(inplace = True)

        corr_inp.sort_values('Correlation', ascending = False).head(10)
        corr_inp = corr_inp.join(ratings['num of ratings'])
        print('Based on your movie ' + inp + ' I think you would like these movies!\n')
        print(corr_inp[corr_inp['num of ratings']>100].sort_values('Correlation', ascending = False).head())




